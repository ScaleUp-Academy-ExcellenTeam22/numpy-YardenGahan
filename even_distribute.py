import numpy as np


def even_distribute():
    """
    This function creates a vector of length 10 with values evenly distributed between 5 and 50.
    :return: vector of values evenly distributed between 5 and 50
    """
    return np.linspace(10, 50, 5)


if __name__ == "__main__":
    print(even_distribute())
