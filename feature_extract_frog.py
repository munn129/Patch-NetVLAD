import argparse
import configparser
import os
from os.path import join, exists, isfile
from os import makedirs

from tqdm.auto import tqdm
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import numpy as np

from patchnetvlad.tools.datasets import PlaceDataset
from patchnetvlad.models.models_generic import get_backend, get_model, get_pca_encoding
from patchnetvlad.tools import PATCHNETVLAD_ROOT_DIR

configfile = './patchnetvlad/configs/mapi_512.ini'
# dataset_file_path
dataset_list = './patchnetvlad/dataset_imagenames/songdo1114_tmp.txt'
dataset_root_dir = '../songdo1114'
output_features_dir = './patchnetvlad/output_features/songdo1114_tmp'
pca_num = '512'

assert os.path.isfile(configfile)
config = configparser.ConfigParser()
config.read(configfile)

if not(torch.cuda.is_available()):
    raise Exception("No CUDA")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

encoder_dim, encoder = get_backend()

dataset = PlaceDataset(None, dataset_list, dataset_root_dir, None, config['feature_extract'])
config['global_params']['num_clusters'] = pca_num
model = get_model(encoder, encoder_dim, config['global_params'], append_pca_layer=True)

model = model.to(device)

### start feature extract

eval_set = dataset

iter_num = 0
avr_time = 0

if not exists(output_features_dir):
    makedirs(output_features_dir)

output_local_features_prefix = join(output_features_dir, 'patchfeats')
output_global_features_filename = join(output_features_dir, 'globalfeats.npy')

pool_size = int(config['global_params']['num_pcs'])

test_data_loader = DataLoader(dataset=eval_set, num_workers=int(config['global_params']['threads']),
                                batch_size=int(config['feature_extract']['cacheBatchSize']),
                                shuffle=False, pin_memory=torch.cuda.is_available())

model.eval()
with torch.no_grad():
    tqdm.write('====> Extracting Features')
    db_feat = np.empty((len(eval_set), pool_size), dtype=np.float32)

    tqdm_instance = tqdm(test_data_loader, position=1, leave=False, desc='Test Iter'.rjust(15))

    for iteration, (input_data, indices) in enumerate(tqdm_instance, 1):
        
        iter_num += 1

        indices_np = indices.detach().numpy()
        input_data = input_data.to(device)
        image_encoding = model.encoder(input_data)
        if config['global_params']['pooling'].lower() == 'patchnetvlad':
            vlad_local, vlad_global = model.pool(image_encoding)

            vlad_global_pca = get_pca_encoding(model, vlad_global)
            db_feat[indices_np, :] = vlad_global_pca.detach().cpu().numpy()

            for this_iter, this_local in enumerate(vlad_local):
                this_patch_size = model.pool.patch_sizes[this_iter]

                db_feat_patches = np.empty((this_local.size(0), pool_size, this_local.size(2)),
                                            dtype=np.float32)
                grid = np.indices((1, this_local.size(0)))
                this_local_pca = get_pca_encoding(model, this_local.permute(2, 0, 1).reshape(-1, this_local.size(1))).\
                    reshape(this_local.size(2), this_local.size(0), pool_size).permute(1, 2, 0)
                db_feat_patches[grid, :, :] = this_local_pca.detach().cpu().numpy()

                for i, val in enumerate(indices_np):
                    image_name = os.path.splitext(os.path.basename(eval_set.images[val]))[0]
                    filename = output_local_features_prefix + '_' + 'psize{}_'.format(this_patch_size) + image_name + '.npy'
                    np.save(filename, db_feat_patches[i, :, :])
        else:
            vlad_global = model.pool(image_encoding)
            vlad_global_pca = get_pca_encoding(model, vlad_global)
            db_feat[indices_np, :] = vlad_global_pca.detach().cpu().numpy()

np.save(output_global_features_filename, db_feat)
print("extract time: {}".format(avr_time))
print("Extracting is done ...")

### end feature extract

torch.cuda.empty_cache()

print('Done')