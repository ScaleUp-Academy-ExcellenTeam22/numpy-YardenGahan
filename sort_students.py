import numpy as np


def sort_student(id_array, height_array):
    """
    This function sorts the student id with increasing height of the students from given students id and height.
    :param id_array: array of id
    :param height_array: array of heights
    :return: none
    """
    indices = np.lexsort((id_array, height_array))
    for index in indices:
        print(id_array[index], height_array[index])


if __name__ == "__main__":
    sort_student([100, 156, 230, 171, 282, 321, 325], [156, 186, 153, 170, 192, 167, 177])
