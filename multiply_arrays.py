import numpy as np


def multiply(array1, array2):
    """
    This function multiplies two given arrays of same size element-by-element.
    :param array1: array of numbers
    :param array2: array of numbers
    :return: array of numbers
    """
    return np.multiply(array1, array2)


if __name__ == "__main__":
    print(multiply(np.arange(9, dtype='int').reshape(-1, 3), np.arange(9, dtype='int').reshape(-1, 3)))
