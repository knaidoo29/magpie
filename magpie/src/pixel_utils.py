import numpy as np
from numba import njit


@njit
def which_pix_id_scalar(x, xmin, dx):
    """
    Finds the pixel index along a defined grid.

    Parameters
    ----------
    x : float
        X-coordinate.
    xmin : float
        Minimum along the grid.
    dx : float
        Pixel width.

    Returns
    -------
    pix_id : int
        The pixel index in which the point is located.
    """
    return int(np.floor((x - xmin) / dx))


@njit
def which_pix_id_array(x, xmin, dx):
    """
    Finds the pixel indices for an array of x-coordinates along a defined grid.

    Parameters
    ----------
    x : array-like (float)
        X-coordinates.
    xmin : float
        Minimum along the grid.
    dx : float
        Pixel width.

    Returns
    -------
    pix_id : array-like (int)
        The pixel indices corresponding to each x value.
    """
    pix_id = np.empty(len(x), dtype=np.int32)
    for i in range(len(x)):
        pix_id[i] = which_pix_id_scalar(x[i], xmin, dx)
    return pix_id
