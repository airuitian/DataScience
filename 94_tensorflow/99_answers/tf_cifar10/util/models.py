"""
    Model define
"""
import tensorflow as tf

from util import loader

model_path = './ckpts/alexnet.ckpt'
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

        # Layer1
        conv1 = tf.layers.conv2d(inputs=self.x, filters=48, kernel_size=(3, 3), activation='relu', padding='same')
        pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=(2, 2), strides=(2, 2), padding='same')

        # Layer2
        conv2 = tf.layers.conv2d(inputs=pool1, filters=128, kernel_size=(3, 3), strides=(2, 2), activation='relu', padding='same')
        pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=(2, 2), strides=(2, 2), padding='same')

        # Layer3
        conv3 = tf.layers.conv2d(inputs=pool2, filters=192, kernel_size=(3, 3), activation='relu', padding='same')

        # Layer4
        conv4 = tf.layers.conv2d(inputs=pool1, filters=192, kernel_size=(3, 3), activation='relu', padding='same')
        pool4 = tf.layers.max_pooling2d(inputs=conv4, pool_size=(2, 2), strides=(2, 2), padding='same')

        # Layer5
        conv5 = tf.layers.conv2d(inputs=pool4, filters=128, kernel_size=(3, 3), activation='relu', padding='same')
        pool5 = tf.layers.max_pooling2d(inputs=conv5, pool_size=(2, 2), strides=(2, 2), padding='same')
        
        flatten = tf.layers.flatten(inputs=pool5)

        fc1 = tf.layers.dense(inputs=flatten, units=4096, activation='relu')

        fc2 = tf.layers.dense(inputs=fc1, units=4096, activation='relu')

        y = tf.layers.dense(inputs=fc2, units=num_classes, activation='softmax')


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
        
        # Model saver
        saver = tf.train.Saver()

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
                    print('\nstep %d, training accuracy %f ' % (step, train_accuracy))
                    print('Model Saved')
                    saver.save(self.sess, model_path, global_step=step)                    
                elif step % 20 == 0:
                    print('.', end='')

        except tf.errors.OutOfRangeError:
            print("End of dataset")
        print(step)

