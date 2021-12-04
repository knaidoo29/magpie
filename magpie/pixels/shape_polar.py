import numpy as np
from matplotlib.patches import Polygon

from . import shape_basic
from . import pix2pos_polar

from .. import utils


def _polar_pixel_polygon(p, r, dr, dp, proj, center, steps, returnpoly):
    """Internal function for returning the polar pixel polygon.

    Parameters
    ----------
    p, r : float
        Pixel coordinate centers.
    dr, dp : float
        Pixel widths.
    proj : str
        Coordinate projection.
    center : list
        Center point of the polar grid, only relevant for cartesian
        projection.
    steps : int
        Number of steps in the polygon.
    returnpoly : bool
        Return matplotlib polygon object.

    Returns
    -------
    x, y : array
        Cartesian or polar coordinate elements for the pixel polygon.
    """
    if proj == 'cart':
        x, y = shape_basic.get_disc(rmin=r-0.5*dr, rmax=r+0.5*dr,
                                     phimin=p-0.5*dp, phimax=p+0.5*dp,
                                     center=center, steps=steps)
    elif proj == 'polar':
        x, y = shape_basic.get_square(xmin=p-0.5*dp, xmax=p+0.5*dp,
                                       ymin=r-0.5*dr, ymax=r+0.5*dr,
                                       steps=steps)
    if returnpoly is True:
        return Polygon(np.column_stack([x, y]))
    else:
        return x, y


def get_polar_shape(pixID, nphi, nr, rmin=0., rmax=1., phimin=0.,
                    phimax=2.*np.pi, proj='cart', center=[0., 0.], steps=12,
                    returnpoly=False):
    """Returns a polygon for the shape of a single polar coordinate pixel in
    polar or cartesian 2D coordinates.

    Parameters
    ----------
    pixID : int
        Pixel index in the polar grid.
    nphi, nr : int
        Grid dimensions along the angular and radial axis.
    rmin, rmax : float, optional
        Radial ranges for the polar grid, default rmin=0 and rmax=1.
    phimin, phimax : float, optional
        Angular ranges for the polar grid, default phimin=0 and phimax=2pi.
    proj : str, optional
        Output coordinate projection. Either 'cart' for cartesian or 'polar'
        for polar projection.
    center : list, optional
        Center point of the polar grid, only relevant for cartesian
        projection, default at the origin.
    steps : int
        Number of steps in the polygon, default=12.
    returnpoly : bool, optional
        Return matplotlib polygon object, default=False.

    Returns
    -------
    x, y or p, r : array
        Cartesian or polar coordinate elements for the pixel polygon.
    """
    assert np.isscalar(pixID), "Must be a single pixel index."
    assert proj == 'cart' or proj == 'polar', \
        "proj must be equal to cart or polar."
    p, r, dp, dr = pix2pos_polar.pix2pos_polar(pixID, nphi, nr, rmin=rmin,
                                               rmax=rmax, phimin=phimin,
                                               phimax=phimax)
    return _polar_pixel_polygon(p, r, dr, dp, proj, center, steps, returnpoly)


def get_polarEA_shape(pixID, nr, rmax=1., base_nphi=4, proj='cart',
                      center=[0., 0.], steps=12, returnpoly=False):
    """Returns a polygon for the shape of a single polar coordinate pixel in
    polar or cartesian 2D coordinates.

    Parameters
    ----------
    pixID : int
        Pixel index.
    nr : int
        Number of divisions along the r-axis.
    rmax : float, optional
        Maximum radial value, default=1.
    base_nphi : int, optional
        Number of pixels around r=0, default=4.
    proj : str, optional
        Output coordinate projection. Either 'cart' for cartesian or 'polar'
        for polar projection.
    center : list, optional
        Center point of the polar grid, only relevant for cartesian
        projection, default at the origin.
    steps : int, optional
        Number of steps in the polygon, default=12.
    returnpoly : bool, optional
        Return matplotlib polygon object, default=False.

    Returns
    -------
    x, y or p, r : array
        Cartesian or polar coordinate elements for the pixel polygon.
    """
    assert np.isscalar(pixID), "Must be a single pixel index."
    assert proj == 'cart' or proj == 'polar', \
        "proj must be equal to cart or polar."
    p, r, dp, dr = pix2pos_polar.pix2pos_polarEA(pixID, nr, rmax=rmax,
                                       base_nphi=base_nphi)
    return _polar_pixel_polygon(p, r, dr, dp, proj, center, steps, returnpoly)
