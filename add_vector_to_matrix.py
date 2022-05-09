import numpy as np


def add_vector_to_matrix(vec, matrix):
    """
    This function adds a given vector to each row of a given matrix.
    :param vec: vector
    :param matrix: matrix
    :return: the matrix after added vector to each line
    """
    rows, cols = matrix.shape
    for i in range(rows):
        matrix[i, :] += vec

    return matrix


if __name__ == "__main__":
    print(add_vector_to_matrix([5, 5, 5, 5], np.arange(0, 16).reshape((4, 4))))