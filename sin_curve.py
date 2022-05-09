import numpy as np
import matplotlib.pyplot as matp


def compute_coordinates():
    """
    This function computes the x and y coordinates for points on a sine curve and plots the points using matplotlib
    :return: None
    """
    x = np.arange(0, 3 * np.pi, 0.2)

    matp.plot(x, np.sin(x))
    matp.show()


if __name__ == "__main__":
    compute_coordinates()
