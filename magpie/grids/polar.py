import numpy as np

from . import cartesian


def polargrid(nr, nphi, rmin=0., rmax=1., phimin=0., phimax=2*np.pi,
              return1d=False):
    """Constructs a polar coordinate grid.

    Parameters
    ----------
    nr : int
        Number of divisions along the r-axis.
    nphi : int
        Number of divisions along the p-axis.
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
    r2d, p2d : 2darray
        Radial and phi grid points in 2darray.
    rmid, pmid : array, optional
        The mid-point of the polar grid.
    """
    if return1d is False:
        r2d, p2d = cartesian.grid2d([rmax-rmin, phimax-phimin], [nr, nphi],
                                    mins=[rmin, phimin], return1d=False)
        return r2d, p2d
    else:
        r2d, p2d, rmid, pmid = \
            cartesian.grid2d([rmax-rmin, phimax-phimin], [nr, nphi],
                             mins=[rmin, phimin], return1d=True)
        return r2d, p2d, rmid, pmid


def polarEA_grid(nr, rmax=1., base_nphi=4):
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
    r, p : array
        Radial and phi mid points for each pixel in the equal area polar grid.
    """
    redges = cartesian.get_xedges(rmax, nr)
    rmid = cartesian.xedges2mid(redges)
    r = np.concatenate([np.array([rmid[i] for j in range(0, base_nphi*(2*i+1))]) for i in range(0, nr)])  # noqa: E501
    p = np.concatenate([cartesian.xedges2mid(cartesian.get_xedges(2*np.pi, base_nphi*(2*i + 1))) for i in range(0, nr)])  # noqa: E501
    return r, p


def polarEA_area(nr, rmax=1., base_nphi=4):
    """Returns the area for an equal area polar grid.

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
    area : float
        The area of pixels in the equal area polar grid.
    """
    area = np.pi * (rmax/nr)**2.
    area /= base_nphi
    return area


def polarEA_npix(nr, base_nphi=4):
    """Returns the number of pixels in an equal area polar grid.

    Parameters
    ----------
    nr : int
        Number of divisions along the r-axis.
    base_nphi : int, optional
        Number of pixels around r=0, default=4.

    Returns
    -------
    npix : int
        Number of pixels in an equal area polar grid.
    """
    npix = base_nphi*nr**2
    return npix
