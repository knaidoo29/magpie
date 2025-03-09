import numpy as np
from numba import njit


@njit
def rotate_2d_scalar(x, y, dphi):
    """
    Rotates a single point (x, y) counter-clockwise by dphi radians.

    Parameters
    ----------
    x, y : float
        Cartesian coordinates.
    dphi : float
        Counter-clockwise rotation in radians.

    Returns
    -------
    xrot, yrot : float
        Rotated x and y coordinates.
    """
    xrot = np.cos(dphi) * x - np.sin(dphi) * y
    yrot = np.sin(dphi) * x + np.cos(dphi) * y
    return xrot, yrot


@njit
def rotate_2d_array(x, y, dphi):
    """
    Rotates an array of points in 2D counter-clockwise by dphi radians.

    Parameters
    ----------
    x, y : array
        Cartesian coordinates of the points.
    dphi : float
        Counter-clockwise rotation in radians.

    Returns
    -------
    xrot, yrot : array
        Rotated x and y coordinates of the points.
    """
    xrot = np.zeros_like(x)
    yrot = np.zeros_like(y)

    for i in range(len(x)):
        xrot[i], yrot[i] = rotate_2d_scalar(x[i], y[i], dphi)

    return xrot, yrot
