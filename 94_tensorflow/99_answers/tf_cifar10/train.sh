#!/bin/sh

rm -rf ./ckpts
rm -rf ./logs
mkdir ./ckpts

#nohup python train.py 128 30 > std.out &
python train.py 128 30 
