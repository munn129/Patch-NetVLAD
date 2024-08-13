#!/usr/bin/env python

# combine feature extract and feature match

from __future__ import print_function

from os.path import join, exists, isfile
from os import makedirs
import argparse
import configparser
import os
import time

from tqdm.auto import tqdm
from torch.utils.data import DataLoader
import torch
import torch.nn as nn
import numpy as np
import faiss
import cv2
from PIL import Image

from patchnetvlad.tools.datasets import PlaceDataset
from patchnetvlad.models.models_generic import get_backend, get_model, get_pca_encoding
from patchnetvlad.models.local_matcher import local_matcher
from patchnetvlad.tools.datasets import input_transform
from patchnetvlad.tools import PATCHNETVLAD_ROOT_DIR

def feature_extract(frame, model, device, config):

    it = input_transform((int(config['feature_extract']['imageresizeh']),
                          int(config['feature_extract']['imageresizew'])))
    input_data = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    input_data = it(input_data).unsqueeze(0)

    pool_size = int(config['global_params']['num_pcs'])

    model.eval()

    with torch.no_grad():

        input_data = input_data.to(device)
        image_encoding = model.encoder(input_data)

        vlad_local, vlad_global = model.pool(image_encoding)

        vlad_global_pca = get_pca_encoding(model, vlad_global)

        for _, this_local in enumerate(vlad_local):

            db_feat_patches = np.empty((this_local.size(0), pool_size, this_local.size(2)),
                                        dtype=np.float32)
            grid = np.indices((1, this_local.size(0)))

            this_local_pca = get_pca_encoding(model, this_local.permute(2, 0, 1).reshape(-1, this_local.size(1))).\
                reshape(this_local.size(2), this_local.size(0), pool_size).permute(1, 2, 0)
            db_feat_patches[grid, :, :] = this_local_pca.detach().cpu().numpy()

    print("Extracting is done ...")

def feature_match(eval_set, device, opt, config):
    input_query_local_features_prefix = join(opt.query_input_features_dir, 'patchfeats')
    input_query_global_features_prefix = join(opt.query_input_features_dir, 'globalfeats.npy')
    input_index_local_features_prefix = join(opt.index_input_features_dir, 'patchfeats')
    input_index_global_features_prefix = join(opt.index_input_features_dir, 'globalfeats.npy')

    qFeat = np.load(input_query_global_features_prefix)
    pool_size = qFeat.shape[1]
    dbFeat = np.load(input_index_global_features_prefix)

    if dbFeat.dtype != np.float32:
        qFeat = qFeat.astype('float32')
        dbFeat = dbFeat.astype('float32')

    tqdm.write('====> Building faiss index')
    faiss_index = faiss.IndexFlatL2(pool_size)
    # noinspection PyArgumentList
    faiss_index.add(dbFeat)

    # n_value is k
    n_values = []
    
    # for n_value in config['feature_match']['n_values_all'].split(","):  # remove all instances of n that are bigger than maxK
    #     n_values.append(int(n_value))
    
    # evaluation code by gym
    # 이부분 11로 바꿔서 할 것
    # for i in range(1, 11):
    #     n_values.append(i)
    # end
    n_values.append(1)

    if config['feature_match']['pred_input_path'] != 'None':
        predictions = np.load(config['feature_match']['pred_input_path'])  # optionally load predictions from a np file
    else:
        # noinspection PyArgumentList
        _, predictions = faiss_index.search(qFeat, min(len(dbFeat), max(n_values)))

    print(predictions)

    reranked_predictions = local_matcher(predictions, eval_set, input_query_local_features_prefix,
                                         input_index_local_features_prefix, config, device)

    print('Finished matching features.')

def main():
    
    parser = argparse.ArgumentParser(description='Patch-NetVLAD-Feature-Extract')
    parser.add_argument('--config_path', type=str, default=join(PATCHNETVLAD_ROOT_DIR, 'configs/performance.ini'),
                        help='File name (with extension) to an ini file that stores most of the configuration data for patch-netvlad')
    parser.add_argument('--dataset_file_path', type=str, required=True,
                        help='Full path (with extension) to a text file that stores the save location and name of all images in the dataset folder')
    parser.add_argument('--dataset_root_dir', type=str, default='',
                        help='If the files in dataset_file_path are relative, use dataset_root_dir as prefix.')
    parser.add_argument('--output_features_dir', type=str, default=join(PATCHNETVLAD_ROOT_DIR, 'output_features'),
                        help='Path to store all patch-netvlad features')
    parser.add_argument('--nocuda', action='store_true', help='If true, use CPU only. Else use GPU.')

    parser.add_argument('--query_file_path', type=str, required=True,
                        help='Path (with extension) to a text file that stores the save location and name of all query images in the dataset')
    parser.add_argument('--index_file_path', type=str, required=True,
                        help='Path (with extension) to a text file that stores the save location and name of all database images in the dataset')
    parser.add_argument('--query_input_features_dir', type=str, required=True,
                        help='Path to load all query patch-netvlad features')
    parser.add_argument('--index_input_features_dir', type=str, required=True,
                        help='Path to load all database patch-netvlad features')

    parser.add_argument('--result_save_folder', type=str, default='results')

    opt = parser.parse_args()
    configfile = opt.config_path
    assert os.path.isfile(configfile)
    config = configparser.ConfigParser()
    config.read(configfile)

    cuda = torch.cuda.is_available()
    if not cuda: raise Exception("No GPU found")

    device = torch.device("cuda" if cuda else "cpu")
    encoder_dim, encoder = get_backend()

    if not os.path.isfile(opt.dataset_file_path):
        opt.dataset_file_path = join(opt.dataset_root_dir, 'dataset_imagenames', opt.dataset_file_path)

    dataset = PlaceDataset(None, opt.dataset_file_path, opt.dataset_root_dir, None, config['feature_extract'])

    # must resume to do extraction
    if config['global_params']['num_pcs'] != '0':
        resume_ckpt = config['global_params']['resumePath'] + config['global_params']['num_pcs'] + '.pth.tar'
    else:
        resume_ckpt = config['global_params']['resumePath'] + '.pth.tar'

    # backup: try whether resume_ckpt is relative to PATCHNETVLAD_ROOT_DIR
    if not isfile(resume_ckpt):
        resume_ckpt = join(PATCHNETVLAD_ROOT_DIR, resume_ckpt)
        if not isfile(resume_ckpt):
            raise Exception("trained file is not exist")

    if isfile(resume_ckpt):
        print("=> loading checkpoint '{}'".format(resume_ckpt))
        checkpoint = torch.load(resume_ckpt, map_location=lambda storage, loc: storage)
        if config['global_params']['num_pcs'] != '0':
            assert checkpoint['state_dict']['WPCA.0.bias'].shape[0] == int(config['global_params']['num_pcs'])
        config['global_params']['num_clusters'] = str(checkpoint['state_dict']['pool.centroids'].shape[0])

        if config['global_params']['num_pcs'] != '0':
            use_pca = True
        else:
            use_pca = False
        model = get_model(encoder, encoder_dim, config['global_params'], append_pca_layer=use_pca)
        model.load_state_dict(checkpoint['state_dict'])
        
        if int(config['global_params']['nGPU']) > 1 and torch.cuda.device_count() > 1:
            model.encoder = nn.DataParallel(model.encoder)
            # if opt.mode.lower() != 'cluster':
            model.pool = nn.DataParallel(model.pool)
       
        model = model.to(device)
        print("=> loaded checkpoint '{}'".format(resume_ckpt, ))
    else:
        raise FileNotFoundError("=> no checkpoint found at '{}'".format(resume_ckpt))
    
    vid = cv2.VideoCapture(0)
    while True:
        _, frame = vid.read()
        feature_extract(frame, model, device, config)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    vid.release()
    cv2.destroyAllWindows()
    torch.cuda.empty_cache()

if __name__ == "__main__":
    main()