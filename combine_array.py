import numpy as np


def combine_array(oned, twod):
    """
    This function combines a one and a two dimensional array together and display their elements.
    :param oned:  one dimensional array
    :param twod:  two dimensional array
    :return:
    """
    for x, y in np.nditer([oned, twod]):
        print(f" {x} : {y}")


if __name__ == "__main__":
    combine_array([1, 2, 3], ([4, 5, 6], [7, 8, 9]))
