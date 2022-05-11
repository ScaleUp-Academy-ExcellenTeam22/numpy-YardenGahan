import numpy as np


def combine_array(oned, twod):
    for x, y in np.nditer([oned, twod]):
        print("%d:%d" % (x, y),)


if __name__ == "__main__":
    print(combine_array([1, 2, 3], ([4, 5, 6], [7, 8, 9])))
