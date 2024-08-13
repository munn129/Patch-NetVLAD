#!/usr/bin/env python

'''
MIT License

Copyright (c) 2021 Stephen Hausler, Sourav Garg, Ming Xu, Michael Milford and Tobias Fischer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Performs place recognition using a two-stage image retrieval pipeline, where
the first step collects the top 100 database candidates and then geometric
verification produces the top 1 best match for every query.

Requires feature_extract.py to be run first, on both a folder of index/database
images and a folder of query images.

Code already supports the datasets of Nordland, Pittsburgh 30k and Tokyo247,
please run tools/genImageListFile to create new imageNames files with your
filepaths pointing to where you saved these datasets (or, edit the text files
to remove the prefix and insert your own prefix).
'''


from __future__ import print_function

import os
import argparse
import configparser
from os.path import join
from os.path import exists
import torch
import numpy as np
import faiss
from tqdm.auto import tqdm
import csv
import time

from patchnetvlad.tools.datasets import PlaceDataset
from patchnetvlad.models.local_matcher import local_matcher
from patchnetvlad.tools import PATCHNETVLAD_ROOT_DIR

CONFIG_PATH = 'patchnetvlad/configs/mapi_512.ini'
DATASET_ROOT_DIR = '~/Documents/Patch-NetVLAD/patchnetvlad'
QUERY_FILE_PATH = 'debug_data.txt'
INDEX_FILE_PATH = 'debug_data.txt'
QUERY_INPUT_FEATURES_DIR = 'patchnetvlad/output_features/debug'
INDEX_INPUT_FEATURES_DIR = 'patchnetvlad/output_features/debug'
RESULT_SAVE_FOLDER = 'patchnetvlad/results/debug'

def write_kapture_output(opt, eval_set, predictions, outfile_name):
    if not exists(opt.result_save_folder):
        os.mkdir(opt.result_save_folder)
    outfile = join(opt.result_save_folder, outfile_name)
    print('Writing results to', outfile)
    with open(outfile, 'w') as kap_out:
        kap_out.write('# kapture format: 1.0\n')
        kap_out.write('# query_image, map_image\n')
        image_list_array = np.array(eval_set.images)
        for q_idx in range(len(predictions)):
            full_paths = image_list_array[predictions[q_idx]]
            query_full_path = image_list_array[eval_set.numDb + q_idx]
            for ref_image_name in full_paths:
                kap_out.write(query_full_path + ', ' + ref_image_name + '\n')


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
        print("========== predictions ==========")
        print(predictions)

    reranked_predictions = local_matcher(predictions, eval_set, input_query_local_features_prefix,
                                         input_index_local_features_prefix, config, device)

    # save predictions to files - Kapture Output
    write_kapture_output(opt, eval_set, predictions, 'NetVLAD_predictions.txt')
    write_kapture_output(opt, eval_set, reranked_predictions, 'PatchNetVLAD_predictions.txt')

    print('Finished matching features.')

def main():
    parser = argparse.ArgumentParser(description='Patch-NetVLAD-Feature-Match')
    parser.add_argument('--config_path', type=str, default=join(PATCHNETVLAD_ROOT_DIR, 'configs/performance.ini'),
                        help='File name (with extension) to an ini file that stores most of the configuration data for patch-netvlad')
    parser.add_argument('--dataset_root_dir', type=str, default='',
                        help='If the files in query_file_path and index_file_path are relative, use dataset_root_dir as prefix.')
    parser.add_argument('--query_file_path', type=str, required=True,
                        help='Path (with extension) to a text file that stores the save location and name of all query images in the dataset')
    parser.add_argument('--index_file_path', type=str, required=True,
                        help='Path (with extension) to a text file that stores the save location and name of all database images in the dataset')
    parser.add_argument('--query_input_features_dir', type=str, required=True,
                        help='Path to load all query patch-netvlad features')
    parser.add_argument('--index_input_features_dir', type=str, required=True,
                        help='Path to load all database patch-netvlad features')
    parser.add_argument('--ground_truth_path', type=str, default=None,
                        help='Path (with extension) to a file that stores the ground-truth data')
    parser.add_argument('--result_save_folder', type=str, default='results')
    parser.add_argument('--posDistThr', type=int, default=None, help='Manually set ground truth threshold')
    parser.add_argument('--nocuda', action='store_true', help='If true, use CPU only. Else use GPU.')

    opt = parser.parse_args()
    print(opt)

    configfile = opt.config_path
    assert os.path.isfile(configfile)
    config = configparser.ConfigParser()
    config.read(configfile)

    cuda = not opt.nocuda
    if cuda and not torch.cuda.is_available():
        raise Exception("No GPU found, please run with --nocuda")

    device = torch.device("cuda" if cuda else "cpu")

    if not os.path.isfile(opt.query_file_path):
        opt.query_file_path = join(PATCHNETVLAD_ROOT_DIR, 'dataset_imagenames', opt.query_file_path)
    if not os.path.isfile(opt.index_file_path):
        opt.index_file_path = join(PATCHNETVLAD_ROOT_DIR, 'dataset_imagenames', opt.index_file_path)

    dataset = PlaceDataset(opt.query_file_path, opt.index_file_path, opt.dataset_root_dir, opt.ground_truth_path,
                           config['feature_extract'], posDistThr=opt.posDistThr)

    start_time = time.time()
    feature_match(dataset, device, opt, config)
    end_time = time.time() - start_time

    torch.cuda.empty_cache()  # garbage clean GPU memory, a bug can occur when Pytorch doesn't automatically clear the
                              # memory after runs
    print('Done')
    print(f'total time: {end_time}')


if __name__ == "__main__":
    main()