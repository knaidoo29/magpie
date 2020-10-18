import numpy as np


def get_randoms_ring_segment(r_min, r_max, phi_min, phi_max, size):
    """Returns randoms inside a ring-segment.

    Parameters
    ----------
    r_min : float
        Minimum r.
    r_max : float
        Maximum r.
    phi_min : float
        Minimum phi.
    phi_max : float
        Maximum phi.
    size : int
        Number of randoms.

    Returns
    -------
    r : array
        Random radial coordinates.
    phi : array
        Random phi coordinates.
    """
    # uniform randoms
    u_r = np.random.random_sample(size)
    u_phi = np.random.random_sample(size)
    # random r and phi within a given range
    r = np.sqrt((r_max**2.-r_min**2.)*u_r + r_min**2.)
    phi = (phi_max-phi_min)*u_phi + phi_min
    return r, phi


def get_randoms_sky_segment(size, phi_min=0., phi_max=2*np.pi, theta_min=0., theta_max=np.pi):
    """
    Random points for a patch of sky (default will give randoms on the full sky). Using the
    coordinate convention phi lies in the range [0, 2pi] and theta lies in the range [0, pi].

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


def get_randoms_sphere_segment(size, r_min=0., r_max=1., phi_min=0., phi_max=2*np.pi, theta_min=0., theta_max=np.pi):
    """
    Random points for a segment of a sphere (default will give randoms within a unit sphere). Using the
    coordinate convention phi lies in the range [0, 2pi] and theta lies in the range [0, pi].

    Parameters
    ----------
    size : int
        Number of randoms to generate.
    r_min : float
        Minimum radius.
    r_max : float
        Maximum radius.
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
    r : array
        Random r.
    phi : array
        Random phi.
    theta : array
        Random theta.
    """
    # uniform randoms
    u_r = np.random.random_sample(size)
    u_phi = np.random.random_sample(size)
    u_theta = np.random.random_sample(size)
    # random phi and theta within a given range
    r = ((r_max**3.-r_min**3.)*u_r + r_min**3.)**(1./3.)
    phi = phi_min + (phi_max - phi_min)*u_phi
    theta = np.arccos(np.cos(theta_min) - (np.cos(theta_min) - np.cos(theta_max))*u_theta)
    return r, phi, theta
