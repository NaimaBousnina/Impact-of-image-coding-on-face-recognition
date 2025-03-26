# coding: utf-8

import argparse
import math
import os
import sys
import time
import glob
import pickle

import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import compressai

from PIL import Image
from torchvision import transforms
from compressai.zoo import cheng2020_anchor

torch.backends.cudnn.deterministic = True
torch.set_num_threads(1)

# general

parser = argparse.ArgumentParser(description='do cheng2020_anchor compression')

parser.add_argument('--Quality-level', default='', type=int, help='1: lowest, highest: 8')
parser.add_argument('--Optimized-metric', default='mse', type=str, help='choose from (‘mse’, ‘ms-ssim’)')
parser.add_argument('--image-path', default='', type=str, help='')
parser.add_argument('--result-dir', default='.', type=str, help='')
parser.add_argument('--result-dir-binary', default='.', type=str, help='')
parser.add_argument('--pretrained', default='True', type=str, help='If True, returns a pre-trained model')
parser.add_argument('--progress', default='True', type=str, help='If True, displays a progress bar of the download to stderr')

args = parser.parse_args()

Quality = args.Quality_level
Metric = args.Optimized_metric
Image_path = args.image_path
Result_dir = args.result_dir
Result_dir_binary = args.result_dir_binary
Pretrained = args.pretrained
Progress = args.progress

@torch.no_grad()
def inference(model, x):
    x = x.unsqueeze(0)
    h, w = x.size(2), x.size(3)
    p = 64  # maximum 6 strides of 2
    new_h = (h + p - 1) // p * p
    new_w = (w + p - 1) // p * p
    padding_left = (new_w - w) // 2
    padding_right = new_w - w - padding_left
    padding_top = (new_h - h) // 2
    padding_bottom = new_h - h - padding_top
    x_padded = F.pad(
        x,
        (padding_left, padding_right, padding_top, padding_bottom),
        mode="constant",
        value=0,
    )

    out_enc = model.compress(x_padded)

    out_dec = model.decompress(out_enc["strings"], out_enc["shape"])

    out_dec["x_hat"] = F.pad(
        out_dec["x_hat"], (-padding_left, -padding_right, -padding_top, -padding_bottom)
    )

    return out_dec["x_hat"], out_enc["strings"]

# Load the pretrained model
net = cheng2020_anchor(quality=Quality, metric= Metric, pretrained=Pretrained).eval()

# Load images 
for filename in glob.glob(Image_path +'/**/*.png'):

    name_0 = os.path.basename(filename).rsplit('_', 1)[0]

    img=Image.open(filename).convert('RGB')
   
    x = transforms.ToTensor()(img)
    
    # Apply the image compression
    out_dec, out_enc = inference(net, x)

    # Convert the Tensor back to a 2D Pillow image
    rec_net = transforms.ToPILImage()(out_dec.squeeze())
    
    # save the reconstracted image to a folder
    name = os.path.basename(filename).rsplit('.', 1)[0]
    print(name)
    rec_net.save(Result_dir + '/' + name_0 +'/' + name +'.png')

    with open(Result_dir_binary + '/' + name_0 +'/'+ name + '.pkl', 'wb') as file:
        save = {
            'Bitstream': out_enc
        }
        pickle.dump(save, file, pickle.HIGHEST_PROTOCOL)