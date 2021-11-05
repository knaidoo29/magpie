import numpy as np
import healpy as hp

from .. import coords


def randoms_sky(size, phi_min=0., phi_max=2*np.pi, theta_min=0., theta_max=np.pi):
    """
    Random points on the sky or more generally across the surface of a sphere. The
    default will give randoms on the full sky.

    Note
    ----
    Coordinate convention:
        - phi lies in the range [0, 2pi]
        - theta lies in the rang [0, pi].

    Parameters
    ----------
    size : int
        Number of randoms to generate.
    phi_min : float
        Minimum longitude in radians.
    phi_max : float
        Maximum longitude in radians.
    theta_min : float
        Minimum latitude in radians.
    theta_max : float
        Maximum longitude in radians.

    Returns
    -------
    phi : array
        Random phi.
    theta : array
        Random theta.
    """
    # uniform randoms
    u_phi = np.random.random_sample(size)
    u_theta = np.random.random_sample(size)
    # random phi and theta within a given range
    phi = phi_min + (phi_max - phi_min)*u_phi
    theta = np.arccos(np.cos(theta_min) - (np.cos(theta_min) - np.cos(theta_max))*u_theta)
    return phi, theta


def randoms_healpix_pixel(size, pix, nside):
    """Returns roughly `size` number of randoms inside a HEALPix pixel.

    Parameters
    ----------
    size : int
        Average number of randoms per pixel.
    pix : int
        Pixel identifier for healpix map.
    nside : int
        Nside of the healpix map.

    Returns
    -------
    phi : array
        Random phi (latitude angle) in radians.
    theta : array
        Random theta (longitude angle) in radians.
    """
    # Find healpix pixel boundaries.
    pix_bound = hp.boundaries(nside, pix, step=1, nest=False)
    theta_bound, phi_bound = hp.vec2ang(pix_bound.T)
    # Check if pixel crosses over the phi 2pi to 0 divide, if it does we shift boundaries below pi by 2pi.
    # shuffle is used to ensure that we know this procedure has been done, and can undo this shift
    # in the generated randoms.
    if phi_bound.max() - phi_bound.min() > np.pi:
        condition = np.where(phi_bound < np.pi)[0]
        phi_bound[condition] += 2.*np.pi
        shuffle = True
    else:
        shuffle = False
    # Calculate the area of the sky segment for which we are actually getting randoms, and compare to the pixel area.
    sky_area = coords.sky_area(phi_bound.min(), phi_bound.max(), theta_bound.min(), theta_bound.max())
    # Adjust the size of randoms to account for the size difference of the pixel vs the sky segment.
    adjusted_size = int(1.05 * size * (sky_area/hp.nside2pixarea(nside)))
    phi_len = 0
    while phi_len < size:
        # Get randoms in the sky segment
        phi_rand, theta_rand = randoms_sky(adjusted_size, phi_min=phi_bound.min(), phi_max=phi_bound.max(),
                                           theta_min=theta_bound.min(), theta_max=theta_bound.max())
        # If shuffle is True we need to shift randoms with phi above 2pi by -2pi.
        if shuffle == True:
            condition = np.where(phi_rand > 2.*np.pi)[0]
            phi_rand[condition] -= 2.*np.pi
        # Cut randoms to only randoms within the desired pixel
        pix_rand = hp.ang2pix(nside, theta_rand, phi_rand)
        condition = np.where(pix_rand == pix)[0]
        _phi, _theta = phi_rand[condition], theta_rand[condition]
        # Concatenate to previous randoms
        if phi_len == 0:
            phi, theta = _phi, _theta
        else:
            phi = np.concatenate([phi, _phi])
            theta = np.concatenate([theta, _theta])
        # check size
        if len(phi) > size:
            phi, theta = phi[:size], theta[:size]
            phi_len = len(phi)
        else:
            phi_len = len(phi)
    return phi, theta
