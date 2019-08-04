import tensorflow as tf

sess = tf.InteractiveSession()

new_saver = tf.train.import_meta_graph('./ckpts/alexnet.ckpt-1600.meta')
for tensor in [tensor.name for tensor in tf.get_default_graph().as_graph_def().node]:
    print(tensor)
def convert_ckpt_frozen(ckpts, step):
    output_nodes = ['output/Softmax']

    ckpts = ckpts + '-' + step
    meta = ckpts + '.meta'
    pb_model = 'frozen_model_step'+'_' + step + '.pb'


    # 1. Load checkpoint files
    saver = tf.train.import_meta_graph(meta, clear_devices=True)
    with tf.Session(graph=tf.get_default_graph()) as sess:
        # Serialize
        input_graph_def = sess.graph.as_graph_def()
        # Load weight
        saver.restore(sess, ckpts)
        # 3. Change variable to constant
        output_graph_def = tf.graph_util.convert_variables_to_constants(sess,
          input_graph_def, output_nodes)
        # Write to pb file
        with open(pb_model, 'wb') as f:
            f.write(output_graph_def.SerializeToString())

convert_ckpt_frozen('./ckpts/alexnet.ckpt', '1600')
