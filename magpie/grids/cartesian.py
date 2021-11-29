import numpy as np

from .. import utils


def get_xedges(length, ngrid, xmin=None):
    """Returns the edges of a uniform grid along one axis.

    Parameters
    ----------
    length : float
        Length of the grid.
    ngrid : int
        Number of grid points.
    xmin : float, optional
        Minimum value of the grid.

    Returns
    -------
    xedges : array
        The edges of a uniform grid along one axis.
    """
    if xmin is None:
        xmin = 0.
    xmax = xmin + length
    xedges = np.linspace(xmin, xmax, ngrid+1)
    return xedges


def xedges2mid(xedges):
    """Returns the mid-point of a uniform grid from the grid edges.

    Parameters
    ----------
    xedges : array
        The edges of a uniform grid along one axis.

    Returns
    -------
    xmid : array
        The mid-point of a uniform grid.
    """
    xmid = 0.5*(xedges[:-1] + xedges[1:])
    return xmid


def xmid2edges(xmid):
    """Returns the mid-point of a uniform grid from the grid edges.

    Parameters
    ----------
    xmid : array
        The mid-point of a uniform grid.

    Returns
    -------
    xedges : array
        The edges of a uniform grid along one axis.
    """
    dx = xmid[1] - xmid[0]
    xedges = np.zeros(len(xmid) + 1)
    xedges[:-1] = xmid - 0.5*dx
    xedges[-1] = xmid[-1] + 0.5*dx
    return xedges


def grid1d(length, ngrid, xmin=None, return_edges=False):
    """Returns the mid-point of a uniform grid.

    Parameters
    ----------
    length : float
        Length of the grid.
    ngrid : int
        Number of grid points.
    xmin : float, optional
        Minimum value of the grid.
    return_edges : bool, optional
        If True then the edges of the uniform grid are also supplied.

    Returns
    -------
    xmid : array
        The mid-point of a uniform grid.
    xedges : array, optional
        The edges of a uniform grid along one axis.
    """
    xedges = get_xedges(length, ngrid, xmin=xmin)
    xmid = xedges2mid(xedges)
    if return_edges is False:
        return xmid
    else:
        return xmid, xedges


def grid2d(lengths, ngrids, mins=[None, None], return1d=False):
    """Returns the mid-point of a uniform grid.

    Parameters
    ----------
    lengths : float or list[float]
        Length of the grid.
    ngrids : int or list[int]
        Number of grid points.
    mins : list[float], optional
        Minimum values of the grid along each axis.
    return1d : bool, optional
        Returns 1d mid-points.

    Returns
    -------
    x2d, y2d : 2darray
        The uniform 2d grid.
    xmid, ymid : array, optional
        The mid-point of the uniform grid.
    """
    if utils.isscalar(lengths) is True:
        _lengths = [lengths, lengths]
    else:
        _lengths = lengths
    if utils.isscalar(ngrids) is True:
        _ngrids = [ngrids, ngrids]
    else:
        _ngrids = ngrids
    xedges = get_xedges(_lengths[0], _ngrids[0], xmin=mins[0])
    xmid = xedges2mid(xedges)
    yedges = get_xedges(_lengths[1], _ngrids[1], xmin=mins[1])
    ymid = xedges2mid(yedges)
    x2d, y2d = np.meshgrid(xmid, ymid, indexing='ij')
    if return1d is False:
        return x2d, y2d
    else:
        return x2d, y2d, xmid, ymid


def grid3d(lengths, ngrids, mins=[None, None, None], return1d=False):
    """Returns the mid-point of a uniform grid.

    Parameters
    ----------
    lengths : float or list[float]
        Length of the grid.
    ngrids : int or list[int]
        Number of grid points.
    mins : list[float], optional
        Minimum values of the grid along each axis.
    return1d : bool, optional
        Returns 1d mid-points.

    Returns
    -------
    x3d, y3d, z3d : 3darray
        The uniform 3d grid.
    xmid, ymid, zmid : array, optional
        The mid-point of the uniform grid.
    """
    if utils.isscalar(lengths) is True:
        _lengths = [lengths, lengths, lengths]
    else:
        _lengths = lengths
    if utils.isscalar(ngrids) is True:
        _ngrids = [ngrids, ngrids, ngrids]
    else:
        _ngrids = ngrids
    xedges = get_xedges(_lengths[0], _ngrids[0], xmin=mins[0])
    xmid = xedges2mid(xedges)
    yedges = get_xedges(_lengths[1], _ngrids[1], xmin=mins[1])
    ymid = xedges2mid(yedges)
    zedges = get_xedges(_lengths[2], _ngrids[2], xmin=mins[2])
    zmid = xedges2mid(zedges)
    x3d, y3d, z3d = np.meshgrid(xmid, ymid, zmid, indexing='ij')
    if return1d is False:
        return x3d, y3d, z3d
    else:
        return x3d, y3d, z3d, xmid, ymid, zmid
