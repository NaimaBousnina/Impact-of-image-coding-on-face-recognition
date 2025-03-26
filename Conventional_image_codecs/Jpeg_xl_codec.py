# coding: utf-8

import argparse
import os
import sys
import glob

parser = argparse.ArgumentParser(description='do JPEG XL compression')

parser.add_argument('--orig-png', default='', type=str, help='')
parser.add_argument('--bitstreams-dir', default='', type=str, help='')
parser.add_argument('--recons-png', default='', type=str, help='')

args = parser.parse_args()

orig_png = args.orig_png
bitstreams_dir = args.bitstreams_dir
recons_png = args.recons_png

img_list = open("Subject_labling.txt")
files = img_list.readlines()

for i in range(len(files)):

	filename, _ = files[i].split()
	name_0 = os.path.basename(filename).rsplit('_', 1)[0]
	name = os.path.basename(filename).rsplit('.', 1)[0]

	#JPEG XL encoder
	bits_result = bitstreams_dir + '/' + name_0 +'/' + name +'.jxl'
	os.system(os.path.join("libjxl/build/tools/cjxl -d 0.25 --strip --resampling=2" + " " + filename + " " + bits_result))

	#JPEG XL decoder
	recon_png_imgs = recons_png + '/' + name_0 +'/' + name +'.png'
	os.system(os.path.join("libjxl/build/tools/djxl" + " " + bits_result + " " + recon_png_imgs))

	print(i)