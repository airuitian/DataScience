"""
    Defines of CNN Layers by tf.nn api
"""
import tensorflow as tf

"""
    Generate weight variable
"""
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


"""
    Generate bias variable
"""
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


"""
    Convolution Layer
"""
def conv2d(inputs, kernel_size, filters, strides=[1, 1, 1, 1], padding='SAME', activate=tf.nn.relu):
    input_channels = inputs.shape.as_list()[-1]
    w_shape = [kernel_size[0], kernel_size[1], input_channels, filters]
    b_shape = [filters]

    conv = tf.nn.conv2d(inputs, weight_variable(w_shape), strides=strides, padding=padding)
    if activate is None:
        return conv + bias_variable(b_shape)

    return activate(conv + bias_variable(b_shape))


"""
    MaxPooling Layer
"""
def max_pooling(inputs, kernel_size=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME'):
    return tf.nn.max_pool(inputs, ksize=kernel_size, strides=strides, padding=padding)


"""
    FC Layer
"""
def fc(inputs, filters, activate=tf.nn.relu):
    inputs_shape = inputs.shape.as_list()
    print(inputs_shape)
    if len(inputs_shape) > 2:
        w = inputs_shape[1]
        h = inputs_shape[2]
        c = inputs_shape[3]
        inputs = tf.reshape(inputs, [-1, w * h * c])
        w = weight_variable([w * h * c, filters])
    else:
        w = weight_variable([inputs_shape[1], filters])

    b = bias_variable([filters])

    if activate is None:
        return tf.matmul(inputs, w) + b

    return tf.nn.relu(tf.matmul(inputs, w) + b)

