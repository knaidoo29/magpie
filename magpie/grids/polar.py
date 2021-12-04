import numpy as np

from . import cartesian


def polargrid(nphi, nr, rmin=0., rmax=1., phimin=0., phimax=2*np.pi,
              return1d=False):
    """Constructs a polar coordinate grid.

    Parameters
    ----------
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
    return1d : bool, optional
        Returns 1d mid-points.

    Returns
    -------
    p2d, r2d : 2darray
        Phi and radial grid points in 2darray.
    pmid, rmid : array, optional
        The mid-point of the polar grid.
    """
    if return1d is False:
        p2d, r2d = cartesian.grid2d([phimax-phimin, rmax-rmin], [nphi, nr],
                                    mins=[phimin, rmin], return1d=False)
        return p2d, r2d
    else:
        p2d, r2d, pmid, rmid = \
            cartesian.grid2d([phimax-phimin, rmax-rmin], [nphi, nr],
                             mins=[phimin, rmin], return1d=True)
        return p2d, r2d, pmid, rmid


def polarEA_grid(nr, rmax=1., base_nphi=3):
    """Constructs an equal area polar grid.

    Parameters
    ----------
    nr : int
        Number of divisions along the r-axis.
    rmax : float, optional
        Maximum radial value, default=1.
    base_nphi : int, optional
        Number of pixels around r=0, default=4.

    Returns
    -------
    p, r : array
        Angular and radial mid points for each pixel in the equal area polar
        grid.
    """
    redges = cartesian.get_xedges(rmax, nr)
    rmid = cartesian.xedges2mid(redges)
    p = np.concatenate([cartesian.xedges2mid(cartesian.get_xedges(2*np.pi, base_nphi*(2*i + 1))) for i in range(0, nr)])  # noqa: E501
    r = np.concatenate([np.array([rmid[i] for j in range(0, base_nphi*(2*i+1))]) for i in range(0, nr)])  # noqa: E501
    return p, r


def polarEA_area(nr, rmax=1., base_nphi=3):
    """Returns the area for an equal area polar grid.

    Parameters
    ----------
    nr : int
        Number of divisions along the r-axis.
    rmax : float, optional
        Maximum radial value, default=1.
    base_nphi : int, optional
        Number of pixels around r=0, default=3.

    Returns
    -------
    area : float
        The area of pixels in the equal area polar grid.
    """
    area = np.pi * (rmax/nr)**2.
    area /= base_nphi
    return area


def polarEA_npix(nr, base_nphi=3):
    """Returns the number of pixels in an equal area polar grid.

    Parameters
    ----------
    nr : int
        Number of divisions along the r-axis.
    base_nphi : int, optional
        Number of pixels around r=0, default=3.

    Returns
    -------
    npix : int
        Number of pixels in an equal area polar grid.
    """
    npix = base_nphi*nr**2
    return npix
