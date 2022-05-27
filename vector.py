import numpy as np


def np_vector():
    """
    This function creates a vector with values from 0 to 20
    and changes the sign of the numbers in the range from 9 to 15.
    :return: numpy vector
    """
    nump_vector = np.arange(21)
    nump_vector[nump_vector >= 9 & nump_vector <= 15] *= -1
    return nump_vector


if __name__ == "__main__":
    print(np_vector())
