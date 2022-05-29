import numpy as np


def remove_dimension(matrix):
    """
    This function removes single-dimensional entries from a given matrix.
    @:arg matrix: a matrix
    :return: The given matrix without single-dimensional entries
    """
    return np.squeeze(shape).shape


if __name__ == "__main__":
    print(remove_dimension([1, 2, 3, 4, 5, 6]))
