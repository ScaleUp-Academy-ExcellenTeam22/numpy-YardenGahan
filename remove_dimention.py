import numpy as np


def remove_dimension(shape):
    """
    This function removes single-dimensional entries from a specified shape.
    @:arg shape: array or list
    :return: The given shape without single-dimensional entries
    """
    return np.squeeze(shape).shape


if __name__ == "__main__":
    print(remove_dimension([1, 2, 3, 4, 5, 6]))
