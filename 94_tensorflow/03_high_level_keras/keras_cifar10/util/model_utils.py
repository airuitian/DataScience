"""
    Utils of models
"""
import tensorflow as tf

"""
    Load keras models(h5)
"""
def load_keras_model(model_path):

    return tf.keras.models.load_model(model_path)
