import tensorflow as tf

import tensorflow as tf

sess = tf.InteractiveSession()

new_saver = tf.train.import_meta_graph('../ckpts/alexnet.ckpt-200.meta')
for tensor in [tensor.name for tensor in tf.get_default_graph().as_graph_def().node]:
    print(tensor)

