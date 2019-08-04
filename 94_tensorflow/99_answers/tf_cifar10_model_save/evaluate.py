import numpy as np
import tensorflow as tf

from util import loader
from sklearn.metrics import classification_report

sess = tf.InteractiveSession()
x_test, y_test = loader.load_cifar10_val_numpy()

frozen_graph_path = './frozen_model_step_1600.pb'

# tf.gfile与python的os模块很像，只不过是优化过的一些操作
# GFile打开一个文件
with tf.gfile.GFile(frozen_graph_path, 'rb') as f:
    # 创建一个GraphDef
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    sess.graph.as_default()
    # 导入计算图
    tf.import_graph_def(graph_def, name='')
 
# 获得输入与输出的tensor
x = sess.graph.get_tensor_by_name('input:0')
y = sess.graph.get_tensor_by_name('output/Softmax:0')

 
predicted = sess.run(y,  feed_dict={x: x_test})
report = classification_report(np.argmax(y_test, axis=1), np.argmax(predicted, axis=1))
print(report)

