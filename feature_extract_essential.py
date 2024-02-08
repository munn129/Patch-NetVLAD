from os.path import isfile

import torch
import torch.nn as nn
import torchvision.models as models
import torchvision

from packaging.version import parse as parse_version

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


# preporcessing
cuda = torch.cuda.is_available()
if not cuda: raise Exception("No CUDA Error")
device = torch.device("cuda" if cuda else "cpu")

encoder_dim = 512
encoder = get_encoder()

# resume_ckpt
weight_file = './pretrained_models/mapillary_WPCA512.pth.tar'
if not isfile(weight_file): raise FileNotFoundError("pretrained model is not exist")
