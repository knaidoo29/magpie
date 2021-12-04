import numpy as np

from .. import grids
from .. import src
from .. import utils


def pix2pos_cart1d(pixID, length, ngrid, xmin=0.):
    """Returns the 1D pixel coordinate from a pixel index.

    Parameters
    ----------
    pixID : int or array
        1D pixel index.
    length : float
        Length of the grid.
    ngrid : int
        Number of grid points.
    xmin : float, optional
        Minimum value of the grid.

    Returns
    -------
    x : float or array
        Mid-point of the pixel points.
    dx : float
        Pixel width.
    """
    dx = length/ngrid
    x = xmin + 0.5*dx + dx*pixID
    return x, dx


def pix2pos_cart2d(pixID, lengths, ngrids, mins=[0., 0.], return1d_pixID=False):
    """Returns the 2D pixel coordinate from a pixel index.

    Parameters
    ----------
    pixID : int or array
        2D pixel index.
    lengths : float or list[float]
        Length of the grid.
    ngrids : int or list[int]
        Number of grid points.
    mins : list[float], optional
        Minimum values of the grid along each axis.
    return1d_pixID : bool, optional
        Returns 1d pixel index.

    Returns
    -------
    x, y : float or array
        Mid-point of the pixel points.
    dx, dy : float
        Pixel width.
    xpixID, ypixID : int or array
        1D pixel index.
    """
    if utils.isscalar(ngrids):
        _ngrids = [ngrids, ngrids]
    else:
        _ngrids = ngrids
    if utils.isscalar(lengths):
        _lengths = [lengths, lengths]
    else:
        _lengths = lengths
    if utils.isscalar(pixID) is True:
        xpixID, ypixID = \
            src.pix_id_2dto1d_scalar(pix_id=pixID, ygrid=_ngrids[1])
    else:
        xpixID, ypixID = \
            src.pix_id_2dto1d_array(pix_id=pixID, xlen=len(pixID),
                                    ygrid=_ngrids[1])
    x = pixID_2_cart1D(xpixID, _ngrids[0], _lengths[0], xmin=mins[0])
    y = pixID_2_cart1D(ypixID, _ngrids[1], _lengths[1], xmin=mins[1])
    dx = _lengths[0]/_ngrids[0]
    dy = _lengths[1]/_ngrids[1]
    if return1d_pixID is False:
        return x, y, dx, dy
    else:
        return x, y, dx, dy, xpixID, ypixID


def pix2pos_cart3d(pixID, lengths, ngrids, mins=[0., 0., 0.],
                   return1d_pixID=False):
    """Returns the 3D pixel coordinate from a pixel index.

    Parameters
    ----------
    pixID : int or array
        3D pixel index.
    lengths : float or list[float]
        Length of the grid.
    ngrids : int or list[int]
        Number of grid points.
    mins : list[float], optional
        Minimum values of the grid along each axis.
    return1d_pixID : bool, optional
        Returns 1d pixel index.

    Returns
    -------
    x, y, z : float or array
        Mid-point of the pixel points.
    dx, dy, dz : float
        Pixel width.
    xpixID, ypixID, zpixID : int or array
        1D pixel index.
    """
    if utils.isscalar(ngrids):
        _ngrids = [ngrids, ngrids, ngrids]
    else:
        _ngrids = ngrids
    if utils.isscalar(lengths):
        _lengths = [lengths, lengths, lengths]
    else:
        _lengths = lengths
    if utils.isscalar(pixID) is True:
        xpixID, ypixID, zpixID = \
            src.pix_id_3dto1d_scalar(pix_id=pixID, ygrid=_ngrids[1],
                                     zgrid=_ngrids[2])
    else:
        xpixID, ypixID, zpixID = \
            src.pix_id_3dto1d_array(pix_id=pixID, xlen=len(pixID),
                                    ygrid=_ngrids[1], zgrid=_ngrids[2])
    x = pixID_2_cart1D(xpixID, _ngrids[0], _lengths[0], xmin=mins[0])
    y = pixID_2_cart1D(ypixID, _ngrids[1], _lengths[1], xmin=mins[1])
    z = pixID_2_cart1D(zpixID, _ngrids[2], _lengths[2], xmin=mins[2])
    dx = _lengths[0]/_ngrids[0]
    dy = _lengths[1]/_ngrids[1]
    dz = _lengths[2]/_ngrids[2]
    if return1d_pixID is False:
        return x, y, z, dx, dy, dz
    else:
        return x, y, z, dx, dy, dz, xpixID, ypixID, zpixID
