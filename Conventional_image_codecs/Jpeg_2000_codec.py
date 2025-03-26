# coding: utf-8

import argparse
import os
import sys
import glob

parser = argparse.ArgumentParser(description='do JPEG 2000 compression')

parser.add_argument('--orig-ppm', default='', type=str, help='')
parser.add_argument('--bitstreams-dir', default='', type=str, help='')
parser.add_argument('--recons-ppm', default='', type=str, help='')
parser.add_argument('--recons-png', default='', type=str, help='')

args = parser.parse_args()

orig_ppm = args.orig_ppm
bitstreams_dir = args.bitstreams_dir
recons_ppm = args.recons_ppm
recons_png = args.recons_png

img_list = open("Subject_labling.txt")
files = img_list.readlines()

for i in range(len(files)): 

	filename, _ = files[i].split()
	name_0 = os.path.basename(filename).rsplit('_', 1)[0]
	name = os.path.basename(filename).rsplit('.', 1)[0]

	# convert png to ppm
	ppm_result = orig_ppm + '/' + name_0 +'/' + name +'.ppm'
	os.system(os.path.join("convert" + " " + filename + " " + "-strip" + " " + ppm_result))

	#JPEG 2000 encoder
	bits_result = bitstreams_dir + '/' + name_0 +'/' + name +'.bits'
	os.system(os.path.join("<path to kdu_compress> -i" + " " + ppm_result + " " + "-o" + " " + bits_result + " " + "-rate 0.25 Qstep=0.001 -tolerance 0 -full -precise -no_weights -num_threads 0"))


	#JPEG decoder
	recon_ppm_imgs = recons_ppm + '/' + name_0 +'/' + name +'.ppm'
	os.system(os.path.join("<path to kdu_expand> -i" + " " + bits_result + " " + "-o" + " " + recon_ppm_imgs + " " + "-precise"))

	# convert ppm to png
	recon_png_imgs = recons_png + '/' + name_0 +'/' + name +'.png'
	os.system(os.path.join("convert" + " " + recon_ppm_imgs + " " + recon_png_imgs))

	print(i)