import argparse
import configparser
import os
from os.path import join, exists, isfile
from os import makedirs

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import numpy as np

from patchnetvlad.tools.datasets import PlaceDataset
from patchnetvlad.models.models_generic import get_backend, get_model, get_pca_encoding
from patchnetvlad.tools import PATCHNETVLAD_ROOT_DIR

if not(torch.cuda.is_available()):
    raise Exception("No CUDA")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

encoder_dim, encoder = get_backend()
