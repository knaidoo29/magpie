import numpy as np

from . import conversions
from . import rotate

from .. import utils


def cart2pov(x, y, z, camera, towards, display, returnall=False):
    """Cartesian coordinates to point-of-view perspective.

    Parameters
    ----------
    x, y, z : float or array
        Cartesian coordinates.
    camera : list
        Cartesian coordinates for the camera.
    towards : list
        The coordinate that the camera points towards.
    display : float
        Distance to the display.
    returnall : bool, optional
        If False only points infront of the screen are returned.

    Returns
    -------
    pov_x, pov_y : float or array
        POV coordinates on the display.
    depth : float or array
        Distance from the camera.
    """
    # recenter directions
    _towards = np.copy(towards)
    _towards[0] = towards[0] - camera[0]
    _towards[1] = towards[1] - camera[1]
    _towards[2] = towards[2] - camera[2]
    _camera = [0, 0, 0]
    # angular directions
    _, _phi_towards, _theta_towards = conversions.cart2sphere(_towards[0], _towards[1],
                                                              _towards[2], center=_camera)
    # places coordinates and direction towards the center of the display
    _x, _y, _z = rotate.rotate3d_Euler(x-camera[0], y-camera[1], z-camera[2],
                                       [-_phi_towards, np.pi/2.-_theta_towards, 0.],
                                       axes='zyz', center=_camera)
    # determines the pov coordinates
    f = display/_x
    if utils.isscalar(_x):
        pov_x = _y*f
        pov_y = _z*f
        depth = np.sqrt(_x**2. + _y**2. + _z**2.)
        if depth >= display or returnall:
            return pov_x, pov_y, depth
        else:
            return None
    else:
        depth = np.sqrt(_x**2. + _y**2. + _z**2.)
        if returnall:
            pov_x = _y*f
            pov_y = _z*f
        else:
            cond = np.where(depth >= display)[0]
            pov_x = _y[cond]*f[cond]
            pov_y = _z[cond]*f[cond]
            depth = depth[cond]
        return pov_x, pov_y, depth


def get_pov_lims(x, y, z, camera, towards, display):
    """Returns the limits of the POV based upon limits of the data in Cartesian
    coordinates.

    Parameters
    ----------
    x, y, z : float or array
        Cartesian coordinates.
    camera : list
        Cartesian coordinates for the camera.
    towards : list
        The coordinate that the camera points towards.
    display : float
        Distance to the display.

    Returns
    -------
    lims : list
        POV limits in [xmin, xmax, ymin, ymax, depthmin, depthmax]
    """
    xx = np.array([np.min(x), np.max(x)])
    yy = np.array([np.min(y), np.max(y)])
    zz = np.array([np.min(z), np.max(z)])
    xx, yy, zz = np.meshgrid(xx, yy, zz, indexing='ij')
    xx = xx.flatten()
    yy = yy.flatten()
    zz = zz.flatten()
    pov_x, pov_y, depth = cart2pov(xx, yy, zz, camera, towards, display, returnall=True)
    pov_lims = [np.min(pov_x), np.max(pov_x), np.min(pov_y),
                np.max(pov_y), np.min(depth), np.max(depth)]
    return pov_lims
