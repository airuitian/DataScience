"""
    Model define
"""
import tensorflow as tf

from tensorflow.keras import layers

num_classes = 10

"""
    Define of AlexNet
"""
def alexnet():
    model = tf.keras.Sequential()
    #Layer 1 
    model.add(layers.Conv2D(48, kernel_size=(3,3),strides=(1,1), activation='relu', padding='same', input_shape=(32, 32, 3)))
    model.add(layers.MaxPooling2D(pool_size=(2,2),strides=(2,2)))

    #Layer 2
    model.add(layers.Conv2D(128, kernel_size=(3,3), activation='relu', padding='same') )
    model.add(layers.MaxPooling2D(pool_size=(2,2),strides=(2,2)))
    
    #Layer 3
    model.add(layers.Conv2D(192, kernel_size=(3,3), activation='relu', padding='same') )
    
    #Layer 4
    model.add(layers.Conv2D(192, kernel_size=(3,3), activation='relu', padding='same') )
    model.add(layers.MaxPooling2D(pool_size=(2,2),strides=(2,2)))
    
    #Layer 5
    model.add(layers.Conv2D(128, kernel_size=(3,3), activation='relu', padding='same') )
    model.add(layers.MaxPooling2D(pool_size=(2,2),strides=(2,2)))
    
    model.add(layers.Flatten())
    
    #Layer 6
    model.add(layers.Dense(4096))
    
    #Layer 7 
    model.add(layers.Dense(4096))
    
    #Prediction
    model.add(layers.Dense(num_classes, activation='softmax'))

    return model
