import numpy as np

from .. import src
from .. import utils


def grid2grid1d(f, boxsize, ngridout, origin=0., originout=0.,
                boxsizeout=None):
    """Remaps a dataset defined on 1D a uniform cartesian grid onto a new 1D
    uniform cartesian grid.

    Parameters
    ----------
    f : array
        The values of the 1D grid pixels.
    boxsize : float
        Box size.
    ngridout : int
        Grid division of the output grid.
    origin : float, optional
        Origin of the grid.
    originout : float, optional
        Origin of the output grid.
    boxsizeout : float
        Box size of the output grid.

    Returns
    -------
    fout : array
        The remapped pixel values for the output 1D grid."""
    x1min = origin
    x1max = origin + boxsize
    x2min = originout
    if boxsizeout is None:
        boxsizeout = boxsize
    x2max = originout + boxsizeout
    fshape = np.shape(f)
    grid1 = fshape[0]
    grid2 = ngridout
    pixlen = src.get_remap_pix_len(x1min=x1min, x1max=x1max, grid1=grid1,
                                   x2min=x2min, x2max=x2max, grid2=grid2)
    fout = src.remap_1d_grid2grid(x1min=x1min, x1max=x1max, grid1=grid1,
                                  x2min=x2min, x2max=x2max, grid2=grid2,
                                  pixlen=pixlen, f1=f)
    return fout


def grid2grid2d(f, boxsize, ngridout, origin=0., originout=0.,
                boxsizeout=None):
    """Remaps a dataset defined on a uniform 2D cartesian grid onto a new
    uniform 2D cartesian grid.

    Parameters
    ----------
    f : 2darray
        The values of the 2D grid pixels.
    boxsize : float or list[float]
        Box size or list of length along each axis.
    ngridout : int or list[int]
        Grid division of the output grid along one axis or a list of the grid
        divisions along each axis.
    origin : float or list[float], optional
        Origin of the grid. If all axes begin at the same origin this can be a
        scalar, if you instead wish to specify different origins for each axis
        this should be added as a list.
    originout : float or list[float], optional
        Origin of the output grid. If all axes begin at the same origin this
        can be a scalar, if you instead wish to specify different origins for
        each axis this should be added as a list.
    boxsizeout : float or list[float], optional
        Box size or list of length along each axis for the output grid.

    Returns
    -------
    fout : 2darray
        The resampled pixel values for the output 2D cartesian grid."""
    if utils.isscalar(boxsize) is True:
        xboxsize, yboxsize = boxsize, boxsize
    else:
        xboxsize, yboxsize = boxsize[0], boxsize[1]
    if boxsizeout is None:
        xboxsizeout, yboxsizeout = xboxsize, yboxsize
    else:
        if utils.isscalar(boxsizeout) is True:
            xboxsizeout, yboxsizeout = boxsizeout, boxsizeout
        else:
            xboxsizeout, yboxsizeout = boxsizeout[0], boxsizeout[1]
    if utils.isscalar(origin) is True:
        xorigin, yorigin = origin, origin
    else:
        xorigin, yorigin = origin[0], origin[1]
    if utils.isscalar(originout) is True:
        xoriginout, yoriginout = originout, originout
    else:
        xoriginout, yoriginout = originout[0], originout[1]
    x1min = xorigin
    x1max = xorigin + xboxsize
    y1min = yorigin
    y1max = yorigin + yboxsize
    x2min = xoriginout
    x2max = xoriginout + xboxsizeout
    y2min = yoriginout
    y2max = yoriginout + yboxsizeout
    fshape = np.shape(f)
    x1grid, y1grid = fshape[0], fshape[1]
    if utils.isscalar(ngridout) is True:
        x2grid, y2grid = ngridout, ngridout
    else:
        x2grid, y2grid = ngridout[0], ngridout[1]
    xpixlen = src.get_remap_pix_len(x1min=x1min, x1max=x1max, grid1=x1grid,
                                    x2min=x2min, x2max=x2max, grid2=x2grid)
    ypixlen = src.get_remap_pix_len(x1min=y1min, x1max=y1max, grid1=y1grid,
                                    x2min=y2min, x2max=y2max, grid2=y2grid)
    f = f.flatten()
    fout = src.remap_2d_grid2grid(x1min=x1min, x1max=x1max, x1grid=x1grid,
                                  y1min=y1min, y1max=y1max, y1grid=y1grid,
                                  x2min=x2min, x2max=x2max, x2grid=x2grid,
                                  y2min=y2min, y2max=y2max, y2grid=y2grid,
                                  xpixlen=xpixlen, ypixlen=ypixlen, f1=f)
    fout = fout.reshape(x2grid, y2grid)
    return fout


def grid2grid3d(f, boxsize, ngridout, origin=0., originout=0.,
                boxsizeout=None):
    """Remaps a dataset defined on 3D cartesian grid onto a new 3D cartesian
    grid.

    Parameters
    ----------
    f : 3darray
        The values of the 3D grid pixels.
    boxsize : float or list[float]
        Box size or list of length along each axis.
    ngridout : int or list[int]
        Grid division of the output grid along one axis or a list of the grid
        divisions along each axis.
    origin : float or list[float], optional
        Origin of the grid. If all axes begin at the same origin this can be a
        scalar, if you instead wish to specify different origins for each axis
        this should be added as a list.
    originout : float or list[float], optional
        Origin of the output grid. If all axes begin at the same origin this
        can be a scalar, if you instead wish to specify different origins for
        each axis this should be added as a list.
    boxsizeout : float or list[float], optional
        Box size or list of length along each axis for the output grid.

    Returns
    -------
    fout : 3darray
        The resampled pixel values for the output 3D cartesian grid."""
    if utils.isscalar(boxsize) is True:
        xboxsize, yboxsize, zboxsize = boxsize, boxsize, boxsize
    else:
        xboxsize, yboxsize, zboxsize = boxsize[0], boxsize[1], boxsize[2]
    if boxsizeout is None:
        xboxsizeout, yboxsizeout, zboxsizeout = xboxsize, yboxsize, zboxsize
    else:
        if utils.isscalar(boxsizeout) is True:
            xboxsizeout, yboxsizeout, zboxsizeout = \
                boxsizeout, boxsizeout, boxsizeout
        else:
            xboxsizeout, yboxsizeout, zboxsizeout = \
                boxsizeout[0], boxsizeout[1], boxsizeout[2]
    if utils.isscalar(origin) is True:
        xorigin, yorigin, zorigin = origin, origin, origin
    else:
        xorigin, yorigin, zorigin = origin[0], origin[1], origin[2]
    if utils.isscalar(originout) is True:
        xoriginout, yoriginout, zoriginout = originout, originout, originout
    else:
        xoriginout, yoriginout, zoriginout = \
            originout[0], originout[1], originout[2]
    x1min = xorigin
    x1max = xorigin + xboxsize
    y1min = yorigin
    y1max = yorigin + yboxsize
    z1min = zorigin
    z1max = zorigin + zboxsize
    x2min = xoriginout
    x2max = xoriginout + xboxsizeout
    y2min = yoriginout
    y2max = yoriginout + yboxsizeout
    z2min = zoriginout
    z2max = zoriginout + zboxsizeout
    fshape = np.shape(f)
    x1grid, y1grid, z1grid = fshape[0], fshape[1], fshape[2]
    if utils.isscalar(ngridout) is True:
        x2grid, y2grid, z2grid = ngridout, ngridout, ngridout
    else:
        x2grid, y2grid, z2grid = ngridout[0], ngridout[1], ngridout[2]
    xpixlen = src.get_remap_pix_len(x1min=x1min, x1max=x1max, grid1=x1grid,
                                    x2min=x2min, x2max=x2max, grid2=x2grid)
    ypixlen = src.get_remap_pix_len(x1min=y1min, x1max=y1max, grid1=y1grid,
                                    x2min=y2min, x2max=y2max, grid2=y2grid)
    zpixlen = src.get_remap_pix_len(x1min=z1min, x1max=z1max, grid1=z1grid,
                                    x2min=z2min, x2max=z2max, grid2=z2grid)
    f = f.flatten()
    fout = src.remap_3d_grid2grid(x1min=x1min, x1max=x1max, x1grid=x1grid,
                                  y1min=y1min, y1max=y1max, y1grid=y1grid,
                                  z1min=z1min, z1max=z1max, z1grid=z1grid,
                                  x2min=x2min, x2max=x2max, x2grid=x2grid,
                                  y2min=y2min, y2max=y2max, y2grid=y2grid,
                                  z2min=z2min, z2max=z2max, z2grid=z2grid,
                                  xpixlen=xpixlen, ypixlen=ypixlen,
                                  zpixlen=zpixlen, f1=f)
    fout = fout.reshape(x2grid, y2grid, z2grid)
    return fout
