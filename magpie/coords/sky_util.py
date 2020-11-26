import numpy as np


def sky_area(phi_min, phi_max, theta_min, theta_max):
    """Returns the area for a 'square' segment of a unit sphere given in
    spherical coordinates phi, theta.

    Parameters
    ----------
    phi_min : float
        Minimum latitudinal coordinate in radians (where phi lies [0, 2pi]).
    phi_max : float
        Maximum latitudinal coordinate in radians (where phi lies [0, 2pi]).
    theta_min : float
        Minimum longitudinal coordinate in radians (where theta lies [0, pi]).
    theta_max : float
        Maximum longitudinal coordinate in radians (where theta lies [0, pi]).

    Returns
    -------
    Area : float
        Area in square radians.
    """
    # check phi ranges lie within allowed ranges
    assert phi_min >= 0. and phi_min < 2.*np.pi, "phi_min must lie within [0, 2pi]."
    assert phi_max > 0. and phi_max <= 2.*np.pi, "phi_max must lie within [0, 2pi]."
    assert phi_min != phi_max, "phi_min cannot equal phi_max."
    assert theta_min >= 0. and theta_min < np.pi, "theta_min must lie within [0, pi]."
    assert theta_max > 0. and theta_max <= np.pi, "theta_max must lie within [0, pi]."
    assert theta_min != theta_max, "theta_min cannot equal theta_max."
    # calculate area
    area = (phi_max - phi_min)*(np.cos(theta_min)-np.cos(theta_max))
    return area
