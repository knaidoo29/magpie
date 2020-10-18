import numpy as np


def cart2polar(x, y, center=[0., 0.]):
    """Return polar coordinates for a given set of cartesian coordinates.

    Parameters
    ----------
    x : array
        x coordinate
    y : array
        y coordinate
    center : list
        Center point of polar coordinate grid.Coordin

    Returns
    -------
    r : array
        Radial coordinate.
    p : array
        Phi coordinate.
    """
    r = np.sqrt((x-center[0])**2. + (y-center[1])**2.)
    p = np.arctan2(y-center[1], x-center[0])
    condition = np.where(p < 0.)
    p[condition] += 2.*np.pi
    return r, p


def polar2cart(r, p, center=[0., 0.]):
    """Return cartesian coordinates for a given set of polar coordinates.

    Parameters
    ----------
    r : array
        Radial coordinate.
    p : array
        Phi coordinate.
    center : list
        Center point of polar coordinate grid.Coordin

    Returns
    -------
    x : array
        x coordinate
    y : array
        y coordinate
    """
    x = r*np.cos(p) + center[0]
    y = r*np.sin(p) + center[1]
    return x, y
