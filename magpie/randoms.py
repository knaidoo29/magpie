import numpy as np


def get_random_ring_segment(rmin, rmax, pmin, pmax, size):
    """Returns randoms inside a ring-segment.

    Parameters
    ----------
    rmin : float
        Minimum r.
    rmax : float
        Maximum r.
    pmin : float
        Minimum phi.
    pmax : float
        Maximum phi.
    size : int
        Number of randoms.

    Returns
    -------
    rrand : array
        Random radial coordinates.
    prand : array
        Random phi coordinates.
    """
    unit_rand = np.random.random_sample(size)
    rrand = np.sqrt((rmax**2.-rmin**2.)*unit_rand + rmin**2.)
    unit_rand = np.random.random_sample(size)
    prand = (pmax-pmin)*unit_rand + pmin
    return rrand, prand
