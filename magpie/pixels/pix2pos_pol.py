import numpy as np

from . import pix2pos_cart

from .. import grids
from .. import utils


def pix2pos_polar(pixID, nphi, nr, rmin=0., rmax=1., phimin=0.,
                  phimax=2.*np.pi, return1d_pixID=False):
    """Returns the 2D pixel coordinate from a pixel index.

    Parameters
    ----------
    pixID : int or array
        2D pixel index.
    nphi : int
        Number of divisions along the p-axis.
    nr : int
        Number of divisions along the r-axis.
    rmin : float, optional
        Minimum radial value, default=0.
    rmax : float, optional
        Maximum radial value, default=1.
    phimin : float, optional
        Minimum phi value, default=0.
    phimax : float, optional
        Maximum phi value, default=2pi.
    return1d_pixID : bool, optional
        Returns 1d pixel index.

    Returns
    -------
    phi, r : float or array
        Mid-point of the pixel points.
    dphi, dr : float
        Pixel width.
    phipixID, rpixID : int or array
        1D pixel index.
    """
    return pix2pos_cart.pix2pos_cart2d(pixID, [phimax-phimin, rmax-rmin],
                                       [nphi, nr], origin=[phimin, rmin],
                                       return1d_pixID=False)


def pix2pos_polarEA(pixID, nr, rmax=1., base_nphi=3):
    """Returns the pixel coordinate on an equal area polar grid.

    Parameters
    ----------
    pixID : int or array
        Pixel index.
    nr : int
        Number of divisions along the r-axis.
    rmax : float, optional
        Maximum radial value, default=1.
    base_nphi : int, optional
        Number of pixels around r=0, default=3.

    Returns
    -------
    p, r : float or array
        Angular and radial mid points for each pixel in the equal area polar
        grid.
    dp, dr : float or array
        Pixel width.
    """
    rpixID = np.floor(np.sqrt(pixID/base_nphi))
    if utils.isscalar(pixID) is True:
        rpixID = int(rpixID)
    else:
        rpixID = rpixID.astype('int')
    ppixID = pixID - grids.polarEA_npix(rpixID, base_nphi=base_nphi)
    dr = rmax/nr
    dp = 2.*np.pi/(base_nphi*(2*rpixID+1))
    r = 0.5*dr + dr*rpixID
    p = 0.5*dp + dp*ppixID
    return p, r, dp, dr
