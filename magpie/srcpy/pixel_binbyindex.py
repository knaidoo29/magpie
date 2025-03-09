import numpy as np
from numba import njit


@njit
def bin_by_index(pix_id, id_weights, pix_len):
    """
    Bins weights by pixel index.

    Parameters
    ----------
    pix_id : array-like (int)
        Pixel indices.
    id_weights : array-like (float)
        Weights corresponding to each index.
    pix_len : int
        Length of the pixel grid.

    Returns
    -------
    pix_val : array-like (float)
        Pixel values after binning.
    """
    pix_val = np.zeros(pix_len, dtype=np.float64)

    for i in range(len(pix_id)):
        if 0 <= pix_id[i] < pix_len:
            pix_val[pix_id[i]] += id_weights[i]

    return pix_val
