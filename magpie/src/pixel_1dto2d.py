import numpy as np
from numba import njit


@njit
def pix_id_1dto2d_scalar(xpix_id, ypix_id, ygrid):
    """
    Returns the combined 2D grid pixel index from pixel indices across each axis.
    
    Parameters
    ----------
    xpix_id : int
        Pixel index along the x-axis grid.
    ypix_id : int
        Pixel index along the y-axis grid.
    ygrid : int
        Length of y-axis grid.
    
    Returns
    -------
    pix_id : int
        2D pixel index.
    """
    if xpix_id != -1 and ypix_id != -1:
        return ypix_id + ygrid * xpix_id
    else:
        return -1


@njit
def pix_id_2dto1d_scalar(pix_id, ygrid):
    """
    Returns the 1D grid pixel indices from a 2D pixel index.
    
    Parameters
    ----------
    pix_id : int
        2D pixel index.
    ygrid : int
        Length of y-axis grid.
    
    Returns
    -------
    xpix_id : int
        Pixel index along the x-axis grid.
    ypix_id : int
        Pixel index along the y-axis grid.
    """
    if pix_id == -1:
        return -1, -1
    else:
        xpix_id = pix_id // ygrid
        ypix_id = int(pix_id - ygrid*xpix_id)
        return xpix_id, ypix_id


@njit
def pix_id_1dto2d_grid(xpix_id, ypix_id, ygrid):
    """
    Maps pixel indices along x and y axes onto a flattened 2D grid.
    
    Parameters
    ----------
    xpix_id : array
        Pixel indices along the x-axis grid.
    ypix_id : array
        Pixel indices along the y-axis grid.
    ygrid : int
        Length of the y-axis grid.
    
    Returns
    -------
    pix_id : array
        Flattened 2D grid pixel indices.
    """
    xlen = len(xpix_id)
    ylen = len(ypix_id)
    pix_id = np.empty(xlen * ylen, dtype=np.int32)
    
    ii = 0
    for i in range(xlen):
        for j in range(ylen):
            pix_id[ii] = pix_id_1dto2d_scalar(xpix_id[i], ypix_id[j], ygrid)
            ii += 1
    
    return pix_id


@njit
def pix_id_1dto2d_array(xpix_id, ypix_id, ygrid):
    """
    Returns the combined grid pixel from pixel indices across each axis.
    
    Parameters
    ----------
    xpix_id : array-like
        Pixel indices along the x-axis grid.
    ypix_id : array-like
        Pixel indices along the y-axis grid.
    ygrid : int
        Length of y-axis grid.
    
    Returns
    -------
    pix_id : array-like
        2D array pixel indices.
    """
    xlen = len(xpix_id)
    pix_id = np.empty(xlen, dtype=np.int32)
    
    for i in range(xlen):
        pix_id[i] = pix_id_1dto2d_scalar(xpix_id[i], ypix_id[i], ygrid)
    return pix_id


@njit
def pix_id_2dto1d_array(pix_id, ygrid):
    """
    Returns the combined grid pixel from pixel indices across each axis.
    
    Parameters
    ----------
    pix_id : array
        2D array pixel indices.
    ygrid : int
        Length of y-axis grid.
    
    Returns
    -------
    xpix_id : array
        Pixel indices along the x-axis grid.
    ypix_id : array
        Pixel indices along the y-axis grid.
    """
    xlen = len(pix_id)
    xpix_id = np.empty(xlen, dtype=np.int32)
    ypix_id = np.empty(xlen, dtype=np.int32)
    
    for i in range(xlen):
        xpix_id[i], ypix_id[i] = pix_id_2dto1d_scalar(pix_id[i], ygrid)
        
    return xpix_id, ypix_id