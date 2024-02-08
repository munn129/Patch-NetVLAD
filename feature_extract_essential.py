from os.path import isfile

import torch
import torch.nn as nn
import torchvision.models as models
import torchvision
import cv2
import numpy as np
from PIL import Image

from packaging.version import parse as parse_version
from patchnetvlad.models.patchnetvlad import PatchNetVLAD
from patchnetvlad.models.frog_models_generic import get_backend ,get_model, get_pca_encoding
from patchnetvlad.tools.datasets import input_transform
from patchnetvlad.models.local_matcher import calc_keypoint_centers_from_patches as calc_keypoint_centers_from_patches



from config import config

def get_encoder():
    if parse_version(torchvision.__version__) >= parse_version('0.13'):
        enc = models.vgg16(weights='IMAGENET1K_V1')
    else:
        enc = models.vgg16(pretrained=True)

    layers = list(enc.features.children())[:-2]
    # only train conv5_1, conv5_2, and conv5_3 (leave rest same as Imagenet trained weights)
    for layer in layers[:-5]:
        for p in layer.parameters():
            p.requires_grad = False
    enc = nn.Sequential(*layers)
    return enc

# cuda setting
cuda = torch.cuda.is_available()
if not cuda: raise Exception("No CUDA Error")
device = torch.device("cuda" if cuda else "cpu")

encoder_dim, encoder = get_backend()

# resume_ckpt
weight_file = config['global_params']['weight_file']
if not isfile(weight_file): raise FileNotFoundError("pretrained model is not exist")

checkpoint = torch.load(weight_file, map_location=lambda storage, loc: storage)
assert checkpoint['state_dict']['WPCA.0.bias'].shape[0] == int(config['global_params']['num_pcs'])
config['global_params']['num_clusters'] = str(checkpoint['state_dict']['pool.centroids'].shape[0])

model = get_model(encoder, encoder_dim, config['global_params'], append_pca_layer=True)
model.load_state_dict(checkpoint['state_dict'])
model = model.to(device)

pool_size = int(config['global_params']['num_pcs'])

# single_image = cv2.imread('../songdo1024/00000.png')
vid = cv2.VideoCapture(0)
while True:
    _, frame = vid.read()
    
    # feature extract 
    model.eval()

    it = input_transform((int(config['feature_extract']['imageresizeh']),
                          int(config['feature_extract']['imageresizew'])))
    im_one_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    im_one_pil = it(im_one_pil).unsqueeze(0)
    input_data = im_one_pil.to(device)

    with torch.no_grad():
        image_encoding = model.encoder(input_data)
        vlad_local, _ = model.pool(image_encoding)
        local_feats = []

        for _, this_local in enumerate(vlad_local):
            this_local_feats = get_pca_encoding(model, this_local.permute(2, 0, 1).reshape(-1, this_local.size(1))). \
                reshape(this_local.size(2), this_local.size(0), pool_size).permute(1, 2, 0)
            local_feats.append(torch.transpose(this_local_feats[0, :, :], 0, 1))

    patch_sizes = [int(s) for s in config['global_params']['patch_sizes'].split(",")]
    strides = [int(s) for s in config['global_params']['strides'].split(",")]
    patch_weights = np.array(config['feature_match']['patchWeights2Use'].split(",")).astype(float)

    all_keypoints = []
    all_indices = []

    for patch_size, stride in zip(patch_sizes, strides):
        # we currently only provide support for square patches, but this can be easily modified for future works
        keypoints, indices = calc_keypoint_centers_from_patches(config['feature_match'], patch_size, patch_size, stride, stride)
        all_keypoints.append(keypoints)
        all_indices.append(indices)
    
    # print(all_keypoints[0])
    display = np.copy(frame)
    for x, y in zip(all_keypoints[0][0], all_keypoints[0][1]):
        cv2.circle(display, (x,y), 5, (255,0,0), -1)

    cv2.imshow('frame', display)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

vid.release()
cv2.destroyAllWindows()
torch.cuda.empty_cache()