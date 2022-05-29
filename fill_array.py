import numpy as np


def fill_array():
    """
    This function creates and sets a three-dimension array with shape and set to a variable.
    Fill the array elements with values using unsigned integer.
    :return: array elements with values using unsigned integer.
    """
    return np.random.randint(low=0, high=255, size=(300, 400, 5))


if __name__ == "__main__":
    print(fill_array())
