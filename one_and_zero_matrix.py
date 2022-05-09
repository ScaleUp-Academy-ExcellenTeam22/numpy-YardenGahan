import numpy as np


def matrix_of_one_and_zero() -> np.matrix:
    """
    This function creates a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0
    :return: matrix in which the elements on the borders will be equal to 1, and inside 0
    """
    matrix = np.ones((10, 10))[1:-1, 1:-1]
    matrix[1:-1, 1:-1] = 0

    return matrix


if __name__ == "__main__":
    print(matrix_of_one_and_zero())