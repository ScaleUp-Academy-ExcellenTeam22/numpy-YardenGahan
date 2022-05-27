import numpy as np


def count_rows_and_cols(matrix) -> str:
    """
    This function finds the number of rows and columns of a given matrix.
    :param matrix: a matrix with x rows and y columns
    :return: number of rows and columns of the matrix
    """
    return f"num of rows and cols is: {matrix.shape}"


if __name__ == "__main__":
    print(count_rows_and_cols(np.arange(0, 30).reshape((5, 6))))
