import numpy as np
from numba import njit


@njit
def pix_id_1dto3d_scalar(xpix_id, ypix_id, zpix_id, ygrid, zgrid):
    """
    Converts 3D pixel indices into a single 1D index.

    Parameters
    ----------
    xpix_id : int
        Pixel index along the x-axis grid.
    ypix_id : int
        Pixel index along the y-axis grid.
    zpix_id : int
        Pixel index along the z-axis grid.
    ygrid : int
        Length of y-axis grid.
    zgrid : int
        Length of z-axis grid.

    Returns
    -------
    pix_id : int
        3D pixel index.
    """
    if xpix_id == -1 or ypix_id == -1 or zpix_id == -1:
        return -1
    else:
        return zpix_id + zgrid * (ypix_id + ygrid * xpix_id)


@njit
def pix_id_3dto1d_scalar(pix_id, ygrid, zgrid):
    """
    Converts a single 1D pixel index back into 3D pixel indices.

    Parameters
    ----------
    pix_id : int
        3D pixel index.
    ygrid : int
        Length of y-axis grid.
    zgrid : int
        Length of z-axis grid.

    Returns
    -------
    xpix_id : int
        Pixel index along the x-axis grid.
    ypix_id : int
        Pixel index along the y-axis grid.
    zpix_id : int
        Pixel index along the z-axis grid.
    """
    if pix_id == -1:
        return -1, -1, -1
    else:
        xypix_id = pix_id // zgrid
        zpix_id = int(pix_id - zgrid*xypix_id)
        xpix_id = xypix_id // ygrid
        ypix_id = int(xypix_id - ygrid*xpix_id)
        return xpix_id, ypix_id, zpix_id


@njit
def pix_id_1dto3d_grid(xpix_id, ypix_id, zpix_id, ygrid, zgrid):
    """
    Maps 3D grid pixel indices to a 1D flattened grid.

    Parameters
    ----------
    xpix_id : array-like
        Pixel indices along the x-axis grid.
    ypix_id : array-like
        Pixel indices along the y-axis grid.
    zpix_id : array-like
        Pixel indices along the z-axis grid.
    ygrid : int
        Length of y-axis grid.
    zgrid : int
        Length of z-axis grid.

    Returns
    -------
    pix_id : array-like
        Flattened 3D grid pixel indices.
    """
    xlen, ylen, zlen = len(xpix_id), len(ypix_id), len(zpix_id)
    pix_id = np.empty(xlen * ylen * zlen, dtype=np.int32)

    ii = 0
    for i in range(xlen):
        for j in range(ylen):
            for k in range(zlen):
                pix_id[ii] = pix_id_1dto3d_scalar(xpix_id[i], ypix_id[j], zpix_id[k], ygrid, zgrid)
                ii += 1

    return pix_id


@njit
def pix_id_1dto3d_array(xpix_id, ypix_id, zpix_id, ygrid, zgrid):
    """
    Converts arrays of 3D pixel indices into a 1D pixel index array.

    Parameters
    ----------
    xpix_id : array-like
        Pixel indices along the x-axis grid.
    ypix_id : array-like
        Pixel indices along the y-axis grid.
    zpix_id : array-like
        Pixel indices along the z-axis grid.
    ygrid : int
        Length of y-axis grid.
    zgrid : int
        Length of z-axis grid.

    Returns
    -------
    pix_id : array-like
        Flattened 3D pixel indices.
    """
    xlen = len(xpix_id)
    pix_id = np.empty(xlen, dtype=np.int32)

    for i in range(xlen):
        pix_id[i] = pix_id_1dto3d_scalar(xpix_id[i], ypix_id[i], zpix_id[i], ygrid, zgrid)

    return pix_id


@njit
def pix_id_3dto1d_array(pix_id, ygrid, zgrid):
    """
    Converts an array of 1D pixel indices into separate x, y, and z pixel index arrays.

    Parameters
    ----------
    pix_id : array-like
        Flattened 3D pixel indices.
    ygrid : int
        Length of y-axis grid.
    zgrid : int
        Length of z-axis grid.

    Returns
    -------
    xpix_id : array-like
        Pixel indices along the x-axis grid.
    ypix_id : array-like
        Pixel indices along the y-axis grid.
    zpix_id : array-like
        Pixel indices along the z-axis grid.
    """
    xlen = len(pix_id)
    xpix_id = np.empty(xlen, dtype=np.int32)
    ypix_id = np.empty(xlen, dtype=np.int32)
    zpix_id = np.empty(xlen, dtype=np.int32)

    for i in range(xlen):
        xpix_id[i], ypix_id[i], zpix_id[i] = pix_id_3dto1d_scalar(pix_id[i], ygrid, zgrid)

    return xpix_id, ypix_id, zpix_id
