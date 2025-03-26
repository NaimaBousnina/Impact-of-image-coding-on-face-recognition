This sub-repository contains the AI-based image codecs adopted by IT to study the impact of image coding on the overall face verification performance. The AI-based image codecs adopted are [Balle2018](https://arxiv.org/pdf/1802.01436.pdf), [Cheng2020](https://arxiv.org/pdf/2001.01568.pdf), and [Hific](https://arxiv.org/pdf/2006.09965.pdf). Balle2018 and Cheng2020 software and codec configurations are those recommended in the [CompressAI](https://interdigitalinc.github.io/CompressAI/zoo.html) evaluation platform, whereas the Hific codec configurations are those recommended in [the official TensorFlow compression GitHub project](https://github.com/tensorflow/compression/tree/master/models/hific).


## 1. How to install the libraries

##### 1.1 CompressAI library requirements

 CompressAI supports python 3.6+ and PyTorch 1.7+

 - pip installation: 

   `pip install compressai`

 - Source installation: 

   `git clone https://github.com/InterDigitalInc/CompressAI compressai`

   `cd compressai`

   `pip install -U pip && pip install -e .`

##### 1.2 Hific library requirements
- Install tensorflow-gpu~=1.15.2+

- Install tensorflow-compression 1.3+

- Install Pillow 8.3.2+

## 2. How to perform the coding

##### 2.1 Commandline-call (examples)

- Balle2018 codec

  `CUDA_VISIBLE_DEVICES=0  python Balle2018.py --Quality-level 1 --image-path lfw/ --result-dir lfw_deompressed_Q1 --result-dir-binary Bitstream_Q1`

- Cheng2020 codec

  `CUDA_VISIBLE_DEVICES=0  python cheng2020.py --Quality-level 1 --image-path lfw/ --result-dir lfw_deompressed_Q1 --result-dir-binary Bitstream_Q1`

- Hific codec

  `CUDA_VISIBLE_DEVICES=0  python hific2020.py --image-path lfw/ --result-dir lfw_deompressed_low --result-dir-binary Bitstream_low`



##### 2.2 Example of decoded images

<table>

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1M0G2NR59f_f_wIgctNS6xswvFr-Xwy5L">
</p>
</table>
