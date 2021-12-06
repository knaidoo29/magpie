import numpy as np

from . import pos2pix_cart

from .. import src
from .. import utils


def pos2pix_polar(phi, r, nphi, nr, phimin=0., phimax=2*np.pi, rmin=0., rmax=1.):
    """Angular and radial coordinates to polar grid.

    Parameters
    ----------
    phi, r : float or array
        Angular and radial coordinates.
    nphi, nr : int
        Grid size along the angular and radial axes.
    phimin, phimax : float, optional
        Angular ranges.
    rmin, rmax : float, optional
        Radial ranges.

    Returns
    -------
    pixID : int or array
        The pixel the points are located in the polar coordinate grid.
    """
    pixID = pos2pix_cart.pos2pix_cart2d(phi, r, [phimax-phimin, rmax-rmin],
                                        [nphi, nr], origin=[phimin, rmin])
    return pixID


def pos2pix_polarEA(phi, r, nr, base_nphi=3, rmax=1.):
    """Angular and radial coordinates to polar equal area grid.

    Parameters
    ----------
    phi, r : float or array
        Angular and radial coordinates.
    nr : int
        Grid size along the radial axes.
    base_nphi : int, optional
        Number of divisions in the angular axes across the first ring.
    rmax : float, optional
        Maximum radius, default=1.

    Returns
    -------
    pixID : int or array
        The pixel index the points are located in the polar coordinate grid.
    """
    dr = rmax/nr
    if utils.isscalar(phi) is True:
        pixID = src.which_pix_id_polar_ea_scalar(r=r, phi=phi, dr=dr,
                                                 base_nphi=base_nphi)
    else:
        pixID = src.which_pix_id_polar_ea_array(r=r, phi=phi, dr=dr,
                                                base_nphi=base_nphi)
    return pixID
