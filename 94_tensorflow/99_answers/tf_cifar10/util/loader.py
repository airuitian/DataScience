"""
    Data loader
"""
import os
import numpy as np

from tensorflow.keras.utils import to_categorical

DATA_PATH = './data/cifar10'

"""
    Load training and validation data set by numpy array
"""
def load_cifar10_numpy():

    x_train = np.load(DATA_PATH + os.sep + 'x_train.npy')
    y_train = np.load(DATA_PATH + os.sep + 'y_train.npy')
    x_test = np.load(DATA_PATH + os.sep + 'x_test.npy')
    y_test = np.load(DATA_PATH + os.sep + 'y_test.npy')

    print('x_train.shape is', x_train.shape)
    print('y_train.shape is', y_train.shape)
    print('x_test.shape is', x_test.shape)
    print('y_test.shape is', y_test.shape)
    
    # normalization
    x_train = x_train / 255
    x_test = x_test / 255

    # one-hot encording
    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)

    return x_train, y_train, x_test, y_test


"""
    Load validation data set by numpy
"""
def load_cifar10_val_numpy():
    x_test = np.load(DATA_PATH + os.sep + 'x_test.npy')
    y_test = np.load(DATA_PATH + os.sep + 'y_test.npy') 

     # normalization
    x_test = x_test / 255

    # one-hot encording
    y_test = to_categorical(y_test, 10)

    return x_test, y_test

