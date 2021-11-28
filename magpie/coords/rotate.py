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


def _rotate3d(x, y, z, rot):
    """Rotate by a given rotation matrix.

    Parameters
    ----------
    x, y, z : float or array
        Cartesian coordinates.
    rot : array
        Rotation matrix.

    Returns
    -------
    xrot, yrot, zrot : float or array
        Rotated x, y and z coordinates.
    """
    if np.isscalar(x) is True:
        xrot, yrot, zrot = src.rotate_3d_scalar(x=x, y=y, z=z, rot=rot)
    else:
        xrot, yrot, zrot = src.rotate_3d_array(x=x, y=y, z=z, rot=rot)
    return xrot, yrot, zrot


def rotate3d_Euler(x, y, z, angles, axes='zyz', center=[0., 0., 0.]):
    """Rotates points in 3D cartesian coordinates by Euler angle around
    specified axes.

    Parameters
    ----------
    x, y, z : float or array
        Cartesian coordinates.
    angles : array
        Euler angles.
    axes : str, optional
        Euler angle axes, default z-y-z rotations.
    center : list[float], optional
        Center of rotation, default=[0., 0., 0.].
    k : array, optional
        If k is specified, points are rotated around a unit vector k.

    Returns
    -------
    xrot, yrot, zrot : float or array
        Rotated x, y and z coordinates.
    """
    assert len(angles) == len(axes), "Length of angles and axes must be consistent."
    assert len(angles) == 3, "Length of angles and axes must be == 3."
    axes_int = []
    for i in range(0, len(axes)):
        if axes[i] == 'x':
            axes_int.append(0)
        elif axes[i] == 'y':
            axes_int.append(1)
        elif axes[i] == 'z':
            axes_int.append(2)
    _x, _y, _z = x-center[0], y-center[1], z-center[2]
    rot = src.rotmat_euler(angles=angles, axes=axes_int)
    _x, _y, _z = _rotate3d(_x, _y, _z, rot)
    xrot = _x + center[0]
    yrot = _y + center[1]
    zrot = _z + center[2]
    return xrot, yrot, zrot


def rotate3d_Rodrigues(x, y, z, k, dphi):
    """Rotates points in 3D cartesian coordinates around an axis defined by the
    unit vector k.

    Parameters
    ----------
    x, y, z : float or array
        Cartesian coordinates.
    k : array
        k is a unit vector k around which points will be rotated by an angle
        dphi.
    dphi : float
        Rodrigues rotation angle around the unit vector k.

    Returns
    -------
    xrot, yrot, zrot : float or array
        Rotated x, y and z coordinates.
    """
    if np.sqrt(np.sum(k**2.)) != 1.:
        k /= np.sqrt(np.sum(k**2.))
    rot = src.rotmat_rodrigues(k=k, dphi=dphi)
    xrot, yrot, zrot = _rotate3d(x, y, z, rot)
    return xrot, yrot, zrot
