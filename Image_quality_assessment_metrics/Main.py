import argparse
import os
import re
import pandas as pd
from metrics import MetricsProcessor, DataClass


def main():

	metrics = MetricsProcessor()

	img_list = open("Subject_labling.txt")
	files = img_list.readlines()

	reco_img_list = '<Path to decompressed images folder'


	bitstreams_list = 'Path to bitstreams folder'

	BPP = []
	ms_ssim = []
	psnr_y = []
	psnr_yuv = []

	for i in range(len(files)):

		print(i)

		ori_filename, _ = files[i].split()

		name_0 = os.path.basename(ori_filename).rsplit('_', 1)[0]
		name = os.path.basename(ori_filename).rsplit('.', 1)[0]

		data_o, target_bd = DataClass().load_image(ori_filename,def_bits=metrics.internal_bits, color_conv=metrics.color_conv)


		recon_filename = reco_img_list + '/' + name_0 +'/' + name +'.png'
		data_r, _ = DataClass().load_image(recon_filename,def_bits=target_bd, color_conv=metrics.color_conv)


		bitstream_filename = bitstreams_list + '/' + name_0 +'/' + name +'.pkl'
		bpp = metrics.bpp_calc(bitstream_filename, data_r.shape)
		BPP.append(bpp)

		metrics_vals = metrics.process_images(data_o, data_r)
		ms_ssim.append(metrics_vals[0])
		psnr_y.append(metrics_vals[1])

		average = (6*metrics_vals[1] + metrics_vals[2] + metrics_vals[3])/8
		psnr_yuv.append(average)


	# Save the values in a excel file.

	df = pd.DataFrame({'BPP': BPP, 'ms_ssim': ms_ssim, 'psnr_y': psnr_y, 'psnr_yuv': psnr_yuv})
	df.to_excel('metrics_assessements.xlsx', sheet_name='metrics', index=False)
	

if __name__ == "__main__":

	main()