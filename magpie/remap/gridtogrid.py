import numpy as np
import shift

from .. import src


def grid2grid2D(d1, boxsize, gridout, sperpix=4):
    """Resamples a dataset defined on 2D cartesian grid onto a new 2D cartesian grid.
    
    Parameters
    ----------
    d1 : array
        The values of the 2D grid pixels.
    boxsize : float
        Size of the box.
    gridout : int
        Size of the output 2D grid along one axis.
    sperpix : int
        The number of samples evenly spaced along each axis for constructing the new 2D grid.

    Returns
    -------
    d2 : array
        The resampled pixel values for the output 2D cartesian grid."""
    gridin = len(d1)
    d1 = d1.flatten()
    xout, yout = shift.cart.grid2d(boxsize, gridout)
    xout = xout.flatten()
    yout = yout.flatten()
    d2 = src.remap_2d_gridtogrid(d1=d1, x=xout, y=yout, boxsize=boxsize,
                                 grid1=gridin, grid2=gridout, sperpix=sperpix)
    d2 = d2.reshape(gridout, gridout)
    return d2


def grid2grid3D(d1, boxsize, gridout, sperpix=4):
    """Resamples a dataset defined on 3D cartesian grid onto a new 3D cartesian grid.

    Parameters
    ----------
    d1 : array
        The values of the 3D grid pixels.
    boxsize : float
        Size of the box.
    gridout : int
        Size of the output 3D grid along one axis.
    sperpix : int
        The number of samples evenly spaced along each axis for constructing the new 3D grid.

    Returns
    -------
    d2 : array
        The resampled pixel values for the output 3D cartesian grid."""
    gridin = len(d1)
    d1 = d1.flatten()
    xout, yout, zout = shift.cart.grid3d(boxsize, gridout)
    xout = xout.flatten()
    yout = yout.flatten()
    zout = zout.flatten()
    d2 = src.remap_3d_gridtogrid(d1=d1, x=xout, y=yout, z=zout, boxsize=boxsize,
                                 grid1=gridin, grid2=gridout, sperpix=sperpix)
    d2 = d2.reshape(gridout, gridout, gridout)
    return d2
