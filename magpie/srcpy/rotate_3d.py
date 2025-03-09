import numpy as np
from numba import njit

from . import math


@njit
def rotmat_x(dphi):
    """
    Rotation matrix for counterclockwise rotation around the x-axis.

    Parameters
    ----------
    dphi : float
        Counter-clockwise rotation angle (in radians).

    Returns
    -------
    rotx : numpy.ndarray
        Rotation matrix around the x-axis.
    """
    rotx = np.zeros(9)
    rotx[0] = 1.0
    rotx[1] = 0.0
    rotx[2] = 0.0
    rotx[3] = 0.0
    rotx[4] = np.cos(dphi)
    rotx[5] = -np.sin(dphi)
    rotx[6] = 0.0
    rotx[7] = np.sin(dphi)
    rotx[8] = np.cos(dphi)
    return rotx


@njit
def rotmat_y(dphi):
    """
    Rotation matrix for counterclockwise rotation around the y-axis.

    Parameters
    ----------
    dphi : float
        Counter-clockwise rotation.

    Returns
    -------
    roty : array
        Rotation matrix around the y-axis.
    """
    roty = np.zeros(9)
    roty[0] = np.cos(dphi)
    roty[1] = 0.0
    roty[2] = np.sin(dphi)
    roty[3] = 0.0
    roty[4] = 1.0
    roty[5] = 0.0
    roty[6] = -np.sin(dphi)
    roty[7] = 0.0
    roty[8] = np.cos(dphi)
    return roty


@njit
def rotmat_z(dphi):
    """
    Rotation matrix for counterclockwise rotation around the z-axis.

    Parameters
    ----------
    dphi : float
        Counter-clockwise rotation.

    Returns
    -------
    rotz : array
        Rotation matrix around the z-axis.
    """
    rotz = np.zeros(9)
    rotz[0] = np.cos(dphi)
    rotz[1] = -np.sin(dphi)
    rotz[2] = 0.0
    rotz[3] = np.sin(dphi)
    rotz[4] = np.cos(dphi)
    rotz[5] = 0.0
    rotz[6] = 0.0
    rotz[7] = 0.0
    rotz[8] = 1.0
    return rotz


@njit
def rotmat_axis(angle, axis):
    """
    Determines the rotation matrix from a specified axis.

    Parameters
    ----------
    angle : float
        Angle of rotation around a given axis.
    axis : int
        Integer of the axis of rotation, where 0=>x-axis, 1=>y-axis, 2=>z-axis.
    
    Returns
    -------
    rot : array
        Rotation matrix.
    """
    if axis == 0:
        return rotmat_x(angle)
    elif axis == 1:
        return rotmat_y(angle)
    elif axis == 2:
        return rotmat_z(angle)
    else:
        raise ValueError("Axis must be 0, 1, or 2.")


@njit
def rotmat_euler(angles, axes):
    """
    Determines the rotation matrix from the Euler angles.

    Parameters
    ----------
    angles : array
        Euler angles.
    axes : array
        Integer array of axes of rotation, where 0=>x-axis, 1=>y-axis, 2=>z-axis.

    Returns
    -------
    rot : array
        Rotation matrix.
    """
    rot1 = rotmat_axis(angles[0], axes[0])
    rot2 = rotmat_axis(angles[1], axes[1])
    rot3 = rotmat_axis(angles[2], axes[2])
    
    rot32 = math.dot3by3(rot3, rot2)
    rot = math.dot3by3(rot32, rot1)
    return rot


@njit
def rotmat_rodrigues(k, dphi):
    """
    Parameters
    ----------
    k : array
        k is a unit vector k around which points will be rotated by an angle dphi.
    dphi : float
        Rodrigues rotation angle around the unit vector k.

    Returns
    -------
    rot : array
        Rotation matrix.
    """
    kmat = np.zeros(9)
    kmat[0] = 0.0
    kmat[1] = -k[2]
    kmat[2] = k[1]
    kmat[3] = k[2]
    kmat[4] = 0.0
    kmat[5] = -k[0]
    kmat[6] = -k[1]
    kmat[7] = k[0]
    kmat[8] = 0.0

    kmat2 = math.dot3by3(kmat, kmat)
    
    rot = np.zeros(9)
    rot[0] = 1. + np.sin(dphi)*kmat[0] + (1. - np.cos(dphi))*kmat2[0]
    rot[1] = np.sin(dphi)*kmat[1] + (1. - np.cos(dphi))*kmat2[1]
    rot[2] = np.sin(dphi)*kmat[3] + (1. - np.cos(dphi))*kmat2[2]

    rot[3] = np.sin(dphi)*kmat[3] + (1. - np.cos(dphi))*kmat2[3]
    rot[4] = 1. + np.sin(dphi)*kmat[4] + (1. - np.cos(dphi))*kmat2[4]
    rot[5] = np.sin(dphi)*kmat[5] + (1. - np.cos(dphi))*kmat2[5]

    rot[6] = np.sin(dphi)*kmat[6] + (1. - np.cos(dphi))*kmat2[6]
    rot[7] = np.sin(dphi)*kmat[7] + (1. - np.cos(dphi))*kmat2[7]
    rot[8] = 1. + np.sin(dphi)*kmat[8] + (1. - np.cos(dphi))*kmat2[8]

    return rot


@njit
def rotate_3d_scalar(x, y, z, rot):
    """
    Rotates a single point in 3D cartesian coordinates by a rotation matrix.
    
    Parameters
    ----------
    x, y, z : float
        Cartesian coordinates.
    rot : float
        Rotation matrix.
    
    Returns
    -------
    xrot, yrot, zrot : float
        Rotated x, y and z coordinates.
    """
    xrot = rot[0] * x + rot[1] * y + rot[2] * z
    yrot = rot[3] * x + rot[4] * y + rot[5] * z
    zrot = rot[6] * x + rot[7] * y + rot[8] * z
    return xrot, yrot, zrot


@njit
def rotate_3d_array(x, y, z, rot):
    """
    Rotates an array of points in 3D cartesian coordinates by a rotation matrix.

    Parameters
    ----------
    x, y, z : array
        Cartesian coordinates.
    rot : float
        Rotation matrix.

    Returns
    -------
    xrot, yrot, zrot : array
        Rotated x, y and z coordinates.
    """
    xlen = len(x)
    xrot = np.zeros(xlen)
    yrot = np.zeros(xlen)
    zrot = np.zeros(xlen)
    
    for i in range(xlen):
        xrot[i], yrot[i], zrot[i] = rotate_3d_scalar(x[i], y[i], z[i], rot)
    
    return xrot, yrot, zrot
