import numpy as np


def unit_metrix():
    """
    This function creates a 3-D array with ones on a diagonal and zeros elsewhere.
    :return: 3-D array with ones on a diagonal and zeros elsewhere.
    """
    return np.identity(3)


if __name__ == "__main__":
    print(unit_metrix())
