# coding: utf-8

import os
import argparse
import tensorflow as tf
import tfci
import glob
from PIL import Image
import numpy as np
import pandas as pd

# Enabling GPU
if not tf.config.list_physical_devices('GPU'):
  print('WARNING: No GPU found. Might be slow!')
else:
  print('Found GPU.')
  
# Only show Warnings 
tf.get_logger().setLevel('WARN')

# general

parser = argparse.ArgumentParser(description='do hific_2020 compression')

parser.add_argument('--Quality-level', default='hific-lo', type=str, help='choose from (‘hific-lo’, ‘hific-mi’, ‘hific-hi’,)')
parser.add_argument('--image-path', default='', type=str, help='')
parser.add_argument('--result-dir', default='.', type=str, help='')
parser.add_argument('--result-dir-binary', default='.', type=str, help='')

args = parser.parse_args()

Quality = args.Quality_level
Image_path = args.image_path
Result_dir = args.result_dir
Result_dir_binary = args.result_dir_binary
  
def read_png(filename):
  """Loads a PNG image file."""
  string = tf.io.read_file(filename)
  image = tf.image.decode_image(string, channels=3)
  return tf.expand_dims(image, 0)

for filename in glob.glob(Image_path +'/**/*.png'):
    print(filename)
    name_0 = os.path.basename(filename).rsplit('_', 1)[0]
    name = os.path.basename(filename).rsplit('.', 1)[0]
    #print(name)

    # Compresse the image
    compressed_path = os.path.join(Result_dir_binary, name_0, f'{name}.tfci')
    bpp, rate = tfci.compress(Quality, filename, compressed_path)

    # Decompresse the image
    output_path = os.path.join(Result_dir, name_0, f'{name}.png')
    output_image = tfci.decompress(compressed_path, output_path)

    if output_image.dtype.is_floating:
      output_image = tf.round(output_image)
    if output_image.dtype != tf.uint8:
      output_image = tf.saturate_cast(output_image, tf.uint8)

    orig = read_png(filename)