import numpy as np


def convert_arrays(array1, array2):
    return np.dstack((array1, array2))


if __name__ == "__main__":
    print(convert_arrays(np.array([10, 20, 30]), np.array([40, 50, 60])))
