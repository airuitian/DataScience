"""
    Model define
"""
import tensorflow as tf

from util import loader
from util import layers

num_classes = 10

"""
    AlexNet Net
"""
class AlexNet_NN:

    """
        Init function
    """
    def __init__(self, batch_size, epochs):
        self.x = tf.placeholder("float", shape=[None, 32, 32, 3])
        # y_: Ground Truth
        self.y_ = tf.placeholder("float", shape=[None, 10])
        self.keep_prob = tf.placeholder("float")
        self.load_data(batch_size, epochs)
        self.sess = tf.InteractiveSession()


    """
        Load training and test data set
    """
    def load_data(self, batch_size, epochs):
        self.x_train, self.y_train, self.x_test, self.y_test = loader.load_cifar10_numpy()

        self.features_placeholder = tf.placeholder(self.x_train.dtype, self.x_train.shape)
        self.labels_placeholder = tf.placeholder(self.y_train.dtype, self.y_train.shape)

        self.dataset = tf.data.Dataset.from_tensor_slices((self.features_placeholder, self.labels_placeholder))
        self.dataset = self.dataset.shuffle(buffer_size=1000)
        self.dataset = self.dataset.repeat(epochs)
        self.dataset = self.dataset.batch(batch_size)


    """
       Forward pass  
    """
    def forward_pass(self):
        conv1 = layers.conv2d(inputs=self.x, kernel_size=[3, 3], filters=48)
        pool1 = layers.max_pooling(conv1)

        conv2 = layers.conv2d(inputs=pool1, kernel_size=[5, 5], filters=64)
        pool2 = layers.max_pooling(conv2)

        fc1 = layers.fc(pool2, filters=1024)
        fc1_drop = tf.nn.dropout(fc1, rate = 1 - self.keep_prob)

        fc2 = layers.fc(fc1_drop, filters=10)

        y = tf.nn.softmax(fc2)

        return y


    """
        Train Function
    """
    def train(self):
        y = self.forward_pass()
        # Loss function
        cross_entropy_map = tf.losses.softmax_cross_entropy(onehot_labels=self.y_, logits=y)
        # Optimizer function
        train_step = tf.train.GradientDescentOptimizer(0.001).minimize(cross_entropy_map)
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(self.y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        self.sess.run(tf.global_variables_initializer())
        
        # Init data set
        iterator = self.dataset.make_initializable_iterator()
        self.sess.run(iterator.initializer, feed_dict={self.features_placeholder: self.x_train, 
            self.labels_placeholder: self.y_train})
        next_element = iterator.get_next()

        step = 1
        try:
            while True:
                batch = self.sess.run(next_element, feed_dict={self.features_placeholder: self.x_train, 
                    self.labels_placeholder: self.y_train})
                features = batch[0]
                label = batch[1]
        
                train_accuracy = accuracy.eval(feed_dict={self.x: features , self.y_: label, self.keep_prob: 1.0})
                train_step.run(feed_dict={self.x: features, self.y_: label, self.keep_prob: 0.5})

                step = step + 1
                if step % 200 == 0:
                    print("\nstep %d, training accuracy %f " % (step, train_accuracy))
                elif step % 20 == 0:
                    print('.', end='')
        
        except tf.errors.OutOfRangeError:
            print("End of dataset")
        print(step)

