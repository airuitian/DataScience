#!/bin/sh

X_TRAIN=./data/cifar10/x_train.npy
Y_TRAIN=./data/cifar10/y_train.npy
X_TEST=./data/cifar10/x_test.npy
Y_TEST=./data/cifar10/y_test.npy

echo "Generating training tfrecord file"
python ./util/generate_tfrecords.py ${X_TRAIN} ${Y_TRAIN} ./cifar10_train.tfrceords
echo "Generating test tfrecord file"
python ./util/generate_tfrecords.py ${X_TEST} ${Y_TEST} ./cifar10_test.tfrceords
