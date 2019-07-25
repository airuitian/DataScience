"""
    Model Tranining
"""
import os
import sys
import numpy as np

from tensorflow.keras.optimizers import SGD
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.callbacks import TensorBoard

from util import loader
from util import models

save_dir = './ckpts'

"""
    Get callbacks
"""
def callbacks():

    # Checkpoint
    filepath="model_{epoch:02d}.hdf5"
    checkpoint = ModelCheckpoint(os.path.join(save_dir, filepath), 
        monitor='val_acc', verbose=1)
    
    # tensorboard
    tb = TensorBoard(log_dir='./logs',
                 histogram_freq=0,  
                 write_graph=True,
                 write_grads=True,
                 write_images=True,
                 )

    return [checkpoint, tb]


"""
    Main Function
"""
def main(batch_size, epochs):
    x_train, y_train, x_test, y_test = loader.load_cifar10_numpy()

    alexnet = models.alexnet()

    # initiate SGD optimizer
    sgd = SGD(lr=0.001, momentum=0.9)

    alexnet.summary()

    alexnet.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    alexnet.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, 
        validation_data=(x_test, y_test), callbacks=callbacks())

if __name__ == '__main__':
    batch_size = int(sys.argv[1])
    epochs = int(sys.argv[2])
    main(batch_size, epochs)
