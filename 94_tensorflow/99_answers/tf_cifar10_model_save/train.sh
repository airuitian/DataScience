#!/bin/sh

rm -rf ./ckpts
rm -rf ./logs
mkdir ./ckpts

python train.py 128 2 
