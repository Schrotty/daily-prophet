#!/bin/bash
cd /usr/src || return
echo "clone sources"
git clone --depth 1 https://code.videolan.org/videolan/x264
git clone git://source.ffmpeg.org/ffmpeg --depth=1
echo "compile h264 support"
cd x264 || return
./configure --host=arm-unknown-linux-gnueabi --enable-static --disable-opencl
make -j4
sudo make install
echo "compile ffmpeg"
cd ../ffmpeg || return
./configure --arch=armel --target-os=linux --enable-gpl --enable-libx264 --enable-nonfree
make -j4
sudo make install