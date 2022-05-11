import numpy as np


def replace_numbers(array, number: int, action: chr):
    """
    This function replaces all numbers in a given array which is equal, less and greater to a given number.
    :param array: array of random numbers
    :param number: number to look for in the array
    :param action: which numbers to replace (smaller, grates or equal to number)
    :return: array
    """
    replace_with = np.pi
    if action == '<':
        return np.where(array < number, replace_with, array)
    if action == '>':
        return np.where(array > number, replace_with, array)
    if action == '=':
        return np.where(array == number, replace_with, array)


if __name__ == "__main__":
    print(replace_numbers(np.arange(16, dtype='int').reshape(-1, 4), 8, '<'))
    print(replace_numbers(np.arange(16, dtype='int').reshape(-1, 4), 8, '>'))
    print(replace_numbers(np.arange(16, dtype='int').reshape(-1, 4), 8, '='))
