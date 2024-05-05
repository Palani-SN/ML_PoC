#!/bin/bash
pp="/home/palani-sn/miniconda3/"
# wget miniconda
if [ ! -f Miniconda3-latest-Linux-x86_64.sh ]; then
    echo "conda not present, downloading from source"
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
fi
if [ ! -f mask_rcnn_coco.h5 ]; then
    echo "mask_rcnn_coco.h5 not present, downloading from source"
    wget https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5
fi
# execute miniconda
if [ ! -f "${pp}bin/conda" ]; then
    echo "conda not present, installing from source"
    sh Miniconda3-latest-Linux-x86_64.sh -b
fi
# set env path
export PATH="${pp}bin:${PATH}"
# check version
conda --version
# initialize
conda init
echo "close and reopen the shell to create and activate conda"
