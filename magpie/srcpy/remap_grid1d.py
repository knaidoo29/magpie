import numpy as np
from numba import njit

from . import remap_utils


@njit
def remap_1d_grid2grid(x1min, x1max, grid1, x2min, x2max, grid2, pixlen, f1):
    """
    Remaps field 1 onto field 2 using exact weights.
    
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
    pixlen : int
        Length of pixel mapping indices and weights.
    f1 : array
        Values on grid 1.

    Returns
    -------
    f2 : array
        Remapped field 1 onto field 2.
    """
    # Initialize the output field f2
    f2 = np.zeros(grid2, dtype=np.float64)

    # Loop over each pixel in grid2 and remap the values
    for i in range(grid2):
        which2pix = i  # pixel in grid 2
        
        # Get the pixel IDs and weights for the current grid 2 pixel
        pix_id, weights = remap_utils.remap_1d_grid2grid_pixel(x1min, x1max, grid1, x2min, x2max, grid2, which2pix, pixlen)
        
        # Initialize the value of f2 at the current pixel
        f2[i] = 0.0
        
        # Sum the weighted values from grid 1 to grid 2
        for j in range(pixlen):
            if pix_id[j] != -1:
                f2[i] += weights[j] * f1[pix_id[j]]

    return f2
