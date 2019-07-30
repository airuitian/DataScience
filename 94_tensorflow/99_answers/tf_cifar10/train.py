"""
    Model Tranining
"""
import sys

from util import models


"""
    Main Function
"""
def main(batch_size, epochs):
    alexnet = models.AlexNet_NN(batch_size, epochs)
    alexnet.train()

if __name__ == '__main__':
    batch_size = int(sys.argv[1])
    epochs = int(sys.argv[2])
    main(batch_size, epochs)

