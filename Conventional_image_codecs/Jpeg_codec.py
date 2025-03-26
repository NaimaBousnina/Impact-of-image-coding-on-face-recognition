# coding: utf-8

import argparse
import os
import sys
import glob

parser = argparse.ArgumentParser(description='do JPEG compression')

parser.add_argument('--orig-pnm', default='', type=str, help='')
parser.add_argument('--bitstreams-dir', default='', type=str, help='')
parser.add_argument('--recons-pnm', default='', type=str, help='')
parser.add_argument('--recons-png', default='', type=str, help='')

args = parser.parse_args()

orig_pnm = args.orig_pnm
bitstreams_dir = args.bitstreams_dir
recons_pnm = args.recons_pnm
recons_png = args.recons_png

img_list = open("Subject_labling.txt")
files = img_list.readlines()

for i in range(len(files)):

	filename, _ = files[i].split()
	name_0 = os.path.basename(filename).rsplit('_', 1)[0]
	name = os.path.basename(filename).rsplit('.', 1)[0]

	# convert png to pnm
	pnm_result = orig_pnm + '/' + name_0 +'/' + name +'.pnm'
	os.system(os.path.join("convert" + " " + filename + " " + "-strip" + " " + pnm_result))

	#JPEG encoder
	bits_result = bitstreams_dir + '/' + name_0 +'/' + name +'.bits'
	os.system(os.path.join("jpeg -q 10 -h -qt 3 -s 1x1,2x2,2x2" + " " + pnm_result + " " + bits_result))

	#JPEG decoder
	recon_pnm_imgs = recons_pnm + '/' + name_0 +'/' + name +'.pnm'
	os.system(os.path.join("jpeg" + " " + bits_result + " " + recon_pnm_imgs))

	# convert pnm to png
	recon_png_imgs = recons_png + '/' + name_0 +'/' + name +'.png'
	os.system(os.path.join("convert" + " " + recon_pnm_imgs + " " + recon_png_imgs))

	print(i)