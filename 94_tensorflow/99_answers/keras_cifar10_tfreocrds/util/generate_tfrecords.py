"""
    Generate tf-record file
"""
import sys
import numpy as np
import tensorflow as tf


def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

"""
    Main Function
"""
def main(img_path, label_path, tfrecords):
    # step 1. 定义一个writer对象
    writer = tf.python_io.TFRecordWriter(tfrecords)

    # Load npy data.
    imgs = np.load(img_path)
    labels = np.load(label_path)

    for _ in range(imgs.shape[0]):

        img = imgs[_]
        label = labels[_][0]
        height = img.shape[0]
        width = img.shape[1]
        img_raw = img.tostring()
        
        # step 2. 定义features
        example = tf.train.Example(features=tf.train.Features(feature={
            'height': _int64_feature(height),
            'width': _int64_feature(width),
            'image_raw': _bytes_feature(img_raw),
            'label': _int64_feature(label)}))
        
        # step 3. 序列化写入
        writer.write(example.SerializeToString())

    writer.close()

if __name__ == '__main__':
    img_path = sys.argv[1]
    label_path = sys.argv[2]
    tfrecords = sys.argv[3]
    main(img_path, label_path, tfrecords)
