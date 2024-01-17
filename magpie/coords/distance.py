import numpy as np

from . import conversions
from . import vector
from .. import utils


def dist1d(x1, x2):
    """Returns the distance between two points in 1D.

    Parameters
    ----------
    x1, x2 : float or array
        Two points for which the distance is required.

    Returns
    -------
    dist : float or array
        Distance between x1 and x2.
    """
    dist = abs(x2 - x1)
    return dist


def dist2d(x1, y1, x2, y2):
    """Returns the distance between two points in 2D.

    Parameters
    ----------
    x1, y1 : float or array
        Location of first points.
    x2, y2 : float or array
        Location of second points.

    Returns
    -------
    dist : float or array
        Distance between point 1 and 2.
    """
    dist = np.sqrt((x2 - x1)**2. + (y2 - y1)**2.)
    return dist


def dist3d(x1, y1, z1, x2, y2, z2):
    """Returns the distance between two points in 3D.

    Parameters
    ----------
    x1, y1, z1 : float or array
        Location of first points.
    x2, y2, z2 : float or array
        Location of second points.

    Returns
    -------
    dist : float or array
        Distance between point 1 and 2.
    """
    dist = np.sqrt((x2 - x1)**2. + (y2 - y1)**2. + (z2 - z1)**2)
    return dist


# def distusphere(phi1, theta1, phi2, theta2):
#     """Compute angular (great-arc) distance between two points on a unit
#     sphere.
#
#     Parameters
#     ----------
#     phi1, theta1 : float or array
#         Location of first points on the unit sphere.
#     phi2, theta2 : float or array
#         Location of second points on the unit sphere.
#
#     Returns
#     -------
#     dist : float or array
#         Angular great-arc distance.
#     """
#     if utils.isscalar(phi1) is True:
#         r = 1.
#     else:
#         r = np.ones(len(phi1))
#     x1, y1, z1 = conversions.sphere2cart(r, phi1, theta1)
#     x2, y2, z2 = conversions.sphere2cart(r, phi2, theta2)
#     dist = np.arccos(x1*x2 + y1*y2 + z1*z2)
#     return dist


def distusphere(phi1, theta1, phi2, theta2):
    """Compute angular (great-arc) distance between two points on a unit
    sphere.

    Parameters
    ----------
    phi1, theta1 : float or array
        Location of first points on the unit sphere.
    phi2, theta2 : float or array
        Location of second points on the unit sphere.

    Returns
    -------
    dist : float or array
        Angular great-arc distance.
    """
    if np.isscalar(phi1) is True:
        r = 1.
    else:
        r = np.ones(len(phi1))
    x1, y1, z1 = conversions.sphere2cart(r, phi1, theta1)
    x2, y2, z2 = conversions.sphere2cart(r, phi2, theta2)
    a = np.array([x1, y1, z1])
    b = np.array([x2, y2, z2])
    cross = vector.vector_cross(a, b)
    normcross = vector.vector_norm(cross)
    dot = vector.vector_dot(a, b)
    dist = np.arctan2(normcross, dot)
    return dist
