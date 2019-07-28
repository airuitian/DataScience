"""
    Data loader
"""
import os
import numpy as np
import tensorflow as tf 

from tensorflow.keras.utils import to_categorical

DATA_PATH = './data/cifar10'
TRAIN_TFRECORD = './cifar10_train.tfrceords'
TEST_TFRECORD = './cifar10_test.tfrceords'

sess=tf.InteractiveSession()


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


"""
    Parse tfrecord
"""
def _parse_function(string_record):
    example = tf.train.Example()
    example.ParseFromString(string_record)
    
    height = int(example.features.feature['height'].int64_list.value[0])
    width = int(example.features.feature['width'].int64_list.value[0])
    img_string = (example.features.feature['image_raw'].bytes_list.value[0])
    label = int(example.features.feature['label'].int64_list.value[0])
 
    img_1d = np.frombuffer(img_string, dtype=np.uint8)
    img = img_1d.reshape((height, width, -1))

    return img, label


"""
    Load training and validation data set by tfrecord files
"""
def load_cifar10_tfrecords(tfrecord):

    dataset = tf.data.TFRecordDataset(tfrecord)
    
    x = []
    y = []

    # 创建Iterator
    sample_iter = dataset.make_one_shot_iterator()
    # 获取next_sample
    next_element = sample_iter.get_next()

    try:
        while True:
            value = sess.run(next_element)
            img, label = _parse_function(value)
            x.append(img / 255)
            y.append(label)
    except:
        pass

    x = np.array(x)
    y = np.array(y)
    # y needs a post processing..
    y = 

    return x, y

