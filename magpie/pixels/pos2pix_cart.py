import numpy as np

from .. import src
from .. import utils


def pos2pix_cart1d(x, length, ngrid, xmin=0.):
    """X-coordinate to 1D pixel.

    Parameters
    ----------
    x : float or array
        X-coordinate.
    length : float
        Length of the 1D grid.
    ngrid : int
        The grid dimension.
    xmin : float, optional
        Minimum value along the grid.

    Returns
    -------
    pixID : int or array
        The index of the pixel the points are located in.
    """
    dx = length/ngrid
    if utils.isscalar(x) is True:
        pixID = src.which_pix_id_scalar(x=x, xmin=xmin, dx=dx)
    else:
        pixID = src.which_pix_id_array(x=x, xmin=xmin, dx=dx, xlen=len(x))
    return pixID


def pos2pix_cart2d(x, y, lengths, ngrids, mins=[0., 0.]):
    """X and Y-coordinate to 2D pixel.

    Parameters
    ----------
    x, y : float or array
        X and Y-coordinate.
    lengths : float or list[float]
        Lengths of the 2D grids.
    ngrids : int or list[int]
        The grid dimension.
    mins : list[float], optional
        Minimum value along the grids.

    Returns
    -------
    pixID : int or array
        The index of the pixel the points are located in 2D.
    """
    if utils.isscalar(lengths):
        _lengths = [lengths, lengths]
    else:
        _lengths = lengths
    if utils.isscalar(ngrids):
        _ngrids = [ngrids, ngrids]
    else:
        _ngrids = ngrids
    xpixID = cart1d_pixID(x, _lengths[0], _ngrids[0], xmins=mins[0])
    ypixID = cart1d_pixID(y, _lengths[1], _ngrids[1], xmins=mins[1])
    if utils.isscalar(x) is True:
        pixID = src.pix_id_1dto2d_scalar(xpix_id=xpixID, ypix_id=ypixID,
                                         ygrid=_ngrids[1])
    else:
        pixID = src.pix_id_1dto2d_array(xpix_id=xpixID, ypix_id=ypixID,
                                        xlen=len(x), ygrid=_ngrids[1])
    return pixID


def pos2pix_cart3d(x, y, z, lengths, ngrids, mins=[0., 0., 0.]):
    """X, Y and Z-coordinate to 3D pixel.

    Parameters
    ----------
    x, y, z : float or array
        X, Y and Z-coordinate.
    lengths : float or list[float]
        Lengths of the 3D grids.
    ngrids : int or list[int]
        The grid dimension.
    mins : list[float], optional
        Minimum value along the grids.

    Returns
    -------
    pixID : int or array
        The index of the pixel the points are located in 3D.
    """
    if utils.isscalar(lengths):
        _lengths = [lengths, lengths, lengths]
    else:
        _lengths = lengths
    if utils.isscalar(ngrids):
        _ngrids = [ngrids, ngrids, ngrids]
    else:
        _ngrids = ngrids
    xpixID = cart1d_pixID(x, _lengths[0], _ngrids[0], xmins=mins[0])
    ypixID = cart1d_pixID(y, _lengths[1], _ngrids[1], xmins=mins[1])
    zpixID = cart1d_pixID(z, _lengths[2], _ngrids[2], xmins=mins[2])
    if utils.isscalar(x) is True:
        pixID = src.pix_id_1dto3d_scalar(xpix_id=xpixID, ypix_id=ypixID,
                                         zpix_id=zpixID, ygrid=_ngrids[1],
                                         zgrid=_ngrids[2])
    else:
        pixID = src.pix_id_1dto3d_array(xpix_id=xpixID, ypix_id=ypixID,
                                        zpix_id=zpixID, xlen=len(x),
                                        ygrid=_ngrids[1], zgrid=_ngrids[2])
    return pixID
