This sub-repository contains the conventional image codecs, e.g. JPEG, JPEG 2000, and JPEG XL adopted by IT to study the impact of image coding on the overall face verification performance. The software and codecs configuration are those recommended in the context of the JPEG AI Call for Proposals.

## 1. How to set-up the software

##### 1.1 JPEG and JPEG 2000 reference software

- Clone the software repository: `git clone https://gitlab.com/wg1/jpeg-ai/jpeg-ai-anchors.git --recursive --shallow-submodules`
- Create conda environment: `conda create -n jpeg_ai_anchors python=3.6.7`
- Activate environment: `conda activate jpeg_ai_anchors`
- Upgrade the `pip`: `python -m pip install --upgrade pip`
- Install the required dependencies: `find . -name "requirement*" -type f -exec pip3 install -r '{}' ';'`
- Install the following packages:

     - FFMPEG 3.4.8
     - Image Magick 6.9.7-4 Q16 20170114
     - CMake 3.10.2 (or above)
     - Autoconf 2.69-11 (or above).

 - Download JPEG2000 binaries from [here](https://kakadusoftware.com/documentation-downloads/downloads/) and uncompress to `Compression/JPEG2000/src/KDU805_Demo_Apps_for_Linux-x86-64_200602`
 - Download JPEG source code from [here](https://jpeg.org/downloads/jpegxt/reference1367abcd89.zip) and uncompress to `Compression/JPEG/src/jpeg_src`

##### 1.2 JPEG XL reference software
- Clone the software repository: `git clone https://github.com/libjxl/libjxl.git --recursive --shallow-submodules`
- Install dependencies:
  - `sudo apt install cmake pkg-config libbrotli-dev libgflags-dev`
  - `sudo apt install libgif-dev libjpeg-dev libopenexr-dev libpng-dev libwebp-dev`

- Install `clang` (version 7 or newer) and set `CC` and `CXX` variables:
  - `sudo apt install clang`
  - `export CC=clang CXX=clang++`

- Build the software:
  - `cd libjxl`
  - `mkdir build`
  - `cd build`
  - `cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF ..`
  - `cmake --build . -- -j$(nproc)`

-  Install the JPEG XL software: `sudo cmake --install .`
## 2. How to use the software

##### 2.1 Commandline-call (examples)
 - JPEG standard: 

   `CUDA_VISIBLE_DEVICES=0 python Jpeg_codec.py --orig-pnm lfw_pnm --bitstreams-dir Bitstream_Q10 --recons-pnm lfw_converted_Q10 --recons-png lfw_deompressed_Q10`
   
- JPEG 2000 standard: 
   
    `CUDA_VISIBLE_DEVICES=0 python Jpeg_2000_codec.py --orig-ppm lfw_ppm --bitstreams-dir Bitstream_R0.25   --recons-ppm lfw_converted_R0.25  --recons-png lfw_deompressed_R0.25`

- JPEG XL standard:

   `CUDA_VISIBLE_DEVICES=0 python Jpeg_xl_codec.py --orig-png lfw --bitstreams-dir Bitstream_R0.25 --recons-png lfw_deompressed_R0.25`

##### 2.2 Example of decompressed images

<table>

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1R3B_ycps_H-_oZ0gKPv-nypiaGBripA-">
</p>
</table>
