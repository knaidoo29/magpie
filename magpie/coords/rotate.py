import numpy as np

from .. import src


def rotate2d(x, y, dphi, center=[0., 0.]):
    """Rotates points in 2D cartesian coordinates counter clockwise by dphi in
    radians.

    Parameters
    ----------
    x, y : float or array
        Cartesian coordinates.
    dphi : float
        Counter-clockwise rotation.
    center : list[float], optional
        Center of rotation, default=[0., 0.].

    Returns
    -------
    xrot, yrot : float or array
        Rotated x and y coordinates.
    """
    if np.isscalar(x) is True:
        xrot, yrot = src.rotate_2d_scalar(x=x-center[0], y=y-center[1], dphi=dphi)
    else:
        xrot, yrot = src.rotate_2d_array(x=x-center[0], y=y-center[1], dphi=dphi)
    xrot += center[0]
    yrot += center[1]
    return xrot, yrot
