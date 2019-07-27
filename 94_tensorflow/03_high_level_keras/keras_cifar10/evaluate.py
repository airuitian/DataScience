"""
    Evaluate model
"""
import sys
import numpy as np

from util import model_utils
from util import loader
from sklearn.metrics import classification_report


def main(model_path):
    model = model_utils.load_keras_model(model_path)

    x_test, y_test = loader.load_cifar10_val_numpy()

    predicted = model.predict(x_test, verbose=1)

    report = classification_report(np.argmax(y_test, axis=1), np.argmax(predicted, axis=1))
    print(report)


if __name__ == '__main__':
    model_path = sys.argv[1]
    main(model_path)
