import numpy as np
from numba import njit

from . import pixel_utils


@njit
def which_pix_id_polar_ea_scalar(r, phi, dr, base_nphi):
    """
    Calculates the pixel index on polar equal area grid of a point in polar coordinates.
    
    Parameters
    ----------
    r : float
        Radial coordinate.
    phi : float
        Angular coordinate.
    dr : float
        Length of radial bins.
    base_nphi : int
        Base phi grid length.

    Returns
    -------
    pix_id : int
        Equal area pixel index.
    """
    # Constants
    pi = 4. * np.arctan(1.0)
    rmin = 0.0
    pmin = 0.0

    # Call to the function for radial index
    rpix_id = pixel_utils.which_pix_id_scalar(r, rmin, dr)

    # Calculate dphi
    dphi = 2 * pi / (base_nphi * (2 * rpix_id + 1))

    # Call to the function for angular index
    phipix_id = pixel_utils.which_pix_id_scalar(phi, pmin, dphi)

    # Pixel index
    pix_id = base_nphi * rpix_id ** 2 + phipix_id

    return pix_id


@njit
def which_pix_id_polar_ea_array(r, phi, dr, base_nphi):
    """
    Calculates the pixel indices on a polar equal area grid of points in polar coordinates.
    
    Parameters
    ----------
    r : array(float)
        Radial coordinates.
    phi : array(float)
        Angular coordinates.
    dr : float
        Length of radial bins.
    base_nphi : int
        Base phi grid length.

    Returns
    -------
    pix_id : array(int)
        Equal area pixel indices.
    """
    rlen = len(r)
    pix_id = np.zeros(rlen, dtype=np.int32)
    
    for i in range(rlen):
        pix_id[i] = which_pix_id_polar_ea_scalar(r[i], phi[i], dr, base_nphi)
    
    return pix_id
