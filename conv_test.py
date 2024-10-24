import os
import sys
import configparser

import torch
import torch.nn as nn
import numpy as np

from PIL import Image
import torchvision.transforms.functional as TF

from patchnetvlad.models.models_generic import get_backend, get_model, get_pca_encoding
sys.path.append('./cosplace')
from cosplace.cosplace_model import cosplace_network, layers

config = configparser.ConfigParser()
config['global_params'] = {
    'pooling' : 'patchnetvlad',
    'resumepath' : './pretrained_models/mapillary_WPCA',
    'threads' : 0,
    'num_pcs' : 512,
    'ngpu' : 1,
    'patch_sizes' : 5,
    'strides' : 1
}

netvlad_pretrained_dir = '/home/moon/Documents/Patch-NetVLAD/patchnetvlad/pretrained_models/mapillary_WPCA512.pth.tar'
cosplace_pretrained_dir = '/home/moon/Documents/Patch-NetVLAD/cosplace/cosplace_resnet152_512.pth'
test_image_dir= '/home/moon/Documents/Patch-NetVLAD/patchnetvlad/tmp_images/1.jpg'

def patch_netvlad_essential(image_tensor, device):
        # patch netvlad start
    encoder_dim, encoder = get_backend() # 512, nn.Sequential(*layers)

    checkpoint = torch.load(netvlad_pretrained_dir)

    config['global_params']['num_clusters'] = str(checkpoint['state_dict']['pool.centroids'].shape[0])

    model = get_model(encoder, encoder_dim, config['global_params'], append_pca_layer=True)
    model.load_state_dict(checkpoint['state_dict'])
    model = model.to(device)

    # feature extract
    pool_size = int(config['global_params']['num_pcs'])

    model.eval()

    with torch.no_grad():
        features = np.empty((1, pool_size), dtype=np.float32)

        image_tensor = image_tensor.to(device)

        image_encoding = model.encoder(image_tensor)

        vlad_local, vlad_global = model.pool(image_encoding)

        vlad_global_pca = get_pca_encoding(model, vlad_global)
        vlad_global_pca = vlad_global_pca.cpu().numpy()

        #patch
        local_feats = []
        for this_iter, this_local in enumerate(vlad_local):
            this_local_feats = get_pca_encoding(model, this_local.permute(2, 0, 1).reshape(-1, this_local.size(1))). \
                reshape(this_local.size(2), this_local.size(0), pool_size).permute(1, 2, 0)
            local_feats.append(torch.transpose(this_local_feats[0, :, :], 0, 1))

        local_feats = local_feats.cpu().numpy()
    # patch net vlad end
    torch.cuda.empty_cache()

def cosplace_essential(image_tensor, device):
     # cosplace start
    model = cosplace_network.GeoLocalizationNet('ResNet152', 512)
    model_state_dict = torch.load(cosplace_pretrained_dir)
    model.load_state_dict(model_state_dict)
    model = model.to(device)
    model.eval()
    
    descriptors = []
    with torch.no_grad():
        descriptors = model(image_tensor.to(device))
        descriptors = descriptors.cpu().numpy()

    # PATCH COSPLACE
    # for this_iter, this_local in enumerate(vlad_local):
    #         this_local_feats = get_pca_encoding(model, this_local.permute(2, 0, 1).reshape(-1, this_local.size(1))). \
    #             reshape(this_local.size(2), this_local.size(0), pool_size).permute(1, 2, 0)
    #         local_feats.append(torch.transpose(this_local_feats[0, :, :], 0, 1))

    # local_feats = local_feats.cpu().numpy()

    # cosplace end
    torch.cuda.empty_cache()

def main():

    test_image = Image.open(test_image_dir)
    image_tensor = TF.to_tensor(test_image)
    image_tensor.unsqueeze_(0)

    if not torch.cuda.is_available():
        raise Exception('No GPU found')
    
    device = torch.device('cuda')

    patch_netvlad_essential(image_tensor, device)
    # cosplace_essential(image_tensor, device)

if __name__ == '__main__':
    main()