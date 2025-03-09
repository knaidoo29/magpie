import numpy as np
from numba import njit

from . import pixel_utils


@njit
def get_remap_pix_len(x1min, x1max, grid1, x2min, x2max, grid2):
    """
    Find pixel weight length for remapping.
    
    Parameters
    ----------
    x1min : float
        Minimum value of grid 1.
    x1max : float
        Maximum value of grid 1.
    grid1 : int
        Number of grid points in grid 1.
    x2min : float
        Minimum value of grid 2.
    x2max : float
        Maximum value of grid 2.
    grid2 : int
        Number of grid points in grid 2.
    
    Returns
    -------
    pixlen : int
        Length of pixel mapping indices and weights.
    """
    # Calculate box sizes and deltas
    boxsize1 = x1max - x1min
    boxsize2 = x2max - x2min
    dx1 = boxsize1 / grid1
    dx2 = boxsize2 / grid2
    
    # Calculate the pixel length
    pixlen = int(np.floor(dx2 / dx1)) + 2
    return pixlen


@njit
def remap_1d_grid2grid_pixel(x1min, x1max, grid1, x2min, x2max, grid2, which2pix, pixlen):
    """
    Computes the exact weights for mapping a single pixel from grid 2 onto grid 1.
    
    Parameters
    ----------
    x1min : float
        Minimum in grid 1.
    x1max : float
        Maximum in grid 1.
    grid1 : int
        Number of grid points in grid 1.
    x2min : float
        Minimum in grid 2.
    x2max : float
        Maximum in grid 2.
    grid2 : int
        Number of grid points in grid 2.
    which2pix : int
        Pixel in grid 2 to be mapped.
    pixlen : int
        Length of pixel mapping indices and weights.
    
    Returns
    -------
    pix_id : array(int)
        Pixels to map from grid 2 to grid 1.
    weights : array(float)
        Weights to map from grid 2 to grid 1.
    """
    # Prepare arrays for output
    pix_id = np.full(pixlen, -1, dtype=np.int32)
    weights = np.zeros(pixlen, dtype=np.float64)

    # Calculate box sizes and deltas
    boxsize1 = x1max - x1min
    boxsize2 = x2max - x2min
    dx1 = boxsize1 / grid1
    dx2 = boxsize2 / grid2
    
    # Calculate edges for grid 2
    x2edge1 = x2min + dx2 * which2pix
    x2edge2 = x2min + dx2 * (which2pix + 1)
    
    # Get the pixel indices for grid 1 from grid 2 edges
    pix1 = pixel_utils.which_pix_id_scalar(x2edge1, x1min, dx1)
    pix2 = pixel_utils.which_pix_id_scalar(x2edge2, x1min, dx1)
    
    if pix1 != pix2:
        for i in range(pixlen):
            pix_id[i] = pix1 + i
            if 0 <= pix_id[i] < grid1:
                x1edge1 = x1min + dx1 * pix_id[i]
                x1edge2 = x1min + dx1 * (pix_id[i] + 1)
                if x2edge1 >= x1edge1 and x2edge2 <= x1edge2:
                    weights[i] = (x2edge2 - x2edge1) / (x2edge2 - x2edge1)
                elif x2edge1 < x1edge1 and x2edge2 <= x1edge2 and x2edge2 > x1edge1:
                    weights[i] = (x2edge2 - x1edge1) / (x2edge2 - x2edge1)
                elif x2edge1 >= x1edge1 and x2edge1 < x1edge2 and x2edge2 > x1edge2:
                    weights[i] = (x1edge2 - x2edge1) / (x2edge2 - x2edge1)
                elif x2edge1 < x1edge1 and x2edge2 > x1edge2:
                    weights[i] = (x1edge2 - x1edge1) / (x2edge2 - x2edge1)
                else:
                    weights[i] = 0.0
                    pix_id[i] = -1
            else:
                weights[i] = 0.0
                pix_id[i] = -1
    elif pix1 != -1:
        for i in range(pixlen):
            pix_id[i] = pix1 + i
            if 0 <= pix_id[i] < grid1:
                if i == 0:
                    weights[i] = 1.0
                else:
                    weights[i] = 0.0
            else:
                weights[i] = 0.0
                pix_id[i] = -1

    return pix_id, weights
