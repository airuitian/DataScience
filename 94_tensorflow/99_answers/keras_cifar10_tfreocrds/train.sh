#!/bin/sh

rm -rf ./ckpts
rm -rf ./logs
mkdir ./ckpts

nohup python train.py 128 10 > std.out &
