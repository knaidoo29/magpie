import numpy as np
import magpie


# AssertionError function

def check_assert(function, *args, **kwargs):
    """Check AssertionError in functions."""
    try:
        function(*args, **kwargs)
    except AssertionError:
        return True

# test conversions.py

def test_cart2polar():
    # check scalar case
    r, p = magpie.coords.cart2polar(0., -1.)
    assert r == 1. and p == 3.*np.pi/2, "Check cart2polar scalar case returns (x, y)=(0, -1) to (r, p)=(0, 3.*np.pi/2)."
    r, p = magpie.coords.cart2polar(0., 1.)
    assert r == 1. and p == np.pi/2., "Check cart2polar scalar case returns (x, y)=(0, 1) to (r, p)=(1, pi/2)."
    # check array case
    x = np.array([1., 0.])
    y = np.array([0., 1.])
    r, p = magpie.coords.cart2polar(x, y)
    assert r[0] == 1. and r[1] == 1. and p[0] == 0. and p[1] == np.pi/2., "Check cart2polar array case."
    # check scalar case + center
    r, p = magpie.coords.cart2polar(0., 2., center=[0., 1.])
    assert r == 1. and p == np.pi/2., "Check cart2polar scalar case with change of center."
    # check array case
    x = np.array([1., 0.])
    y = np.array([1., 2.])
    r, p = magpie.coords.cart2polar(x, y, center=[0., 1.])
    assert r[0] == 1. and r[1] == 1. and p[0] == 0. and p[1] == np.pi/2., "Check cart2polar array case with change of center."

def test_polar2cart():
    x, y = magpie.coords.polar2cart(1., np.pi/2.)
    assert np.round(x, 1) == 0. and y == 1., "Check polar2cart (r, p) = (1., pi/2) returns (x, y) = (0., 1.)."
    x, y = magpie.coords.polar2cart(1., np.pi/2., center=[0., 1.])
    assert np.round(x, 1) == 0. and y == 2., "Check polar2cart (r, p) = (1., pi/2) with center (0., 1.) returns (x, y)=(0., 2.)."

def test_cart2sphere():
    # scalar case
    r, phi, theta = magpie.coords.cart2sphere(0., 0., 0.)
    assert r == 0. and phi == 0. and theta == 0., "Check cart2sphere (x, y, z) = (0., 0., 0.) returns (r, p, t) = (0., 0., 0.)."
    r, phi, theta = magpie.coords.cart2sphere(0., -1., 0.)
    assert r == 1. and phi == 3*np.pi/2. and theta == np.pi/2., "Check cart2sphere (x, y, z) = (0., -1., 0.) returns (r, p, t) = (1., 3pi/2, pi/2)."
    r, phi, theta = magpie.coords.cart2sphere(1., 0., 0.)
    assert r == 1. and phi == 0. and theta == np.pi/2., "Check cart2sphere (x, y, z) = (1., 0., 0.) returns (r, p, t) = (1., 0., pi/2)."
    r, phi, theta = magpie.coords.cart2sphere(1., 0., 0., center=[1., 0., 1.])
    assert r == 1. and phi == 0. and theta == np.pi, "Check cart2sphere (x, y, z) = (1., 0., 0.) with center = (1., 0., 1.) returns (r, p, t) = (1., 0., pi)."
    # array case
    x = np.array([0., 1.])
    y = np.array([0., 1.])
    z = np.array([0., 1.])
    r, p, t = magpie.coords.cart2sphere(x, y, z)
    assert r[0] == 0. and p[0] == 0. and t[0] == 0., "Check cart2sphere (x, y, z) = (0., 0., 0) for array."
    assert np.round(r[1], 2) == 1.73 and np.round(p[1], 2) == 0.79 and np.round(t[1], 2) == 0.96,  "Check cart2sphere (x, y, z) = (1., 1., 1.) for array."
    r, p, t = magpie.coords.cart2sphere(x, y, z, center=[1., 1., 1.])
    assert r[1] == 0. and p[1] == 0. and t[1] == 0., "Check cart2sphere (x, y, z) = (0., 0., 0) for array with center (1., 1., 1.)."
    assert np.round(r[0], 2) == 1.73 and np.round(p[0], 2) == 3.93 and np.round(t[0], 2) == 2.19,  "Check cart2sphere (x, y, z) = (1., 1., 1.) for array."

def test_sphere2cart():
    x, y, z = magpie.coords.sphere2cart(1., 0., 0.)
    assert x == 0. and y == 0. and z == 1., "Check sphere2cart (r, p, t) = (1., 0., 0.) returns (x, y, z) = (0., 0., 1.)."
    x, y, z = magpie.coords.sphere2cart(1., 0., np.pi/2., center=[0.5, 0.5, 0.5])
    assert x == 1.5 and y == 0.5 and np.round(z, 1) == 0.5, "Check sphere2cart (r, p, t) = (1., 0., pi/2.) with center (0.5, 0.5, 0.5) returns (x, y, z) = (1.5, 0.5, 0.5)."

def test_ortho2cart():
    z = magpie.coords.ortho2cart(0., 0., r=1., fill_value=np.nan)
    assert z == 1., "Check ortho2cart (x, y) = (0., 0.)."
    z = magpie.coords.ortho2cart(2., 0., r=1., fill_value=np.nan)
    assert np.isnan(z), "Check ortho2cart (x, y) = (2., 0.)."
    x = np.array([0., 2.])
    y = np.array([0., 0.])
    z = magpie.coords.ortho2cart(x, y, r=1., fill_value=np.nan)
    assert z[0] == 1., "Check ortho2cart (x, y) = (0., 0.)."
    assert np.isnan(z[1]), "Check ortho2cart (x, y) = (2., 0.)."

# test usphere_util.py

def test_usphere_area_assert_phi_min_less_zero():
    assert check_assert(magpie.coords.usphere_area, *[-0.1, 2., 0., 2.]), "Check phi_min < 0. returns assertion error."

def test_usphere_area_assert_phi_min_more_2pi():
    assert check_assert(magpie.coords.usphere_area, *[2.*np.pi+0.1, 2., 0., 2.]), "Check phi_min > 2pi returns assertion error."

def test_usphere_area_assert_phi_max_less_zero():
    assert check_assert(magpie.coords.usphere_area, *[0., -0.1, 0., 2.]), "Check phi_max < 0. returns assertion error."

def test_usphere_area_assert_phi_max_more_2pi():
    assert check_assert(magpie.coords.usphere_area, *[0., 2.*np.pi+0.1, 0., 2.]), "Check phi_max > 2pi returns assertion error."

def test_usphere_area_assert_phi_min_equals_phi_max():
    assert check_assert(magpie.coords.usphere_area, *[0., 0., 0., 2.]), "Check phi_min = phi_max returns assertion error."

def test_usphere_area_assert_theta_min_less_zero():
    assert check_assert(magpie.coords.usphere_area, *[0., 2., -0.1, 2.]), "Check theta_min < 0. returns assertion error."

def test_usphere_area_assert_theta_min_more_pi():
    assert check_assert(magpie.coords.usphere_area, *[0., 2., np.pi+0.1, 2.]), "Check theta_min > pi returns assertion error."

def test_usphere_area_assert_theta_max_less_zero():
    assert check_assert(magpie.coords.usphere_area, *[0., 2., -0.1, 2.]), "Check theta_max < 0. returns assertion error."

def test_usphere_area_assert_theta_max_more_2pi():
    assert check_assert(magpie.coords.usphere_area, *[0., 2., np.pi+0.1, 2.]), "Check theta_max > 2pi returns assertion error."

def test_usphere_area_assert_theta_min_equals_theta_max():
    assert check_assert(magpie.coords.usphere_area, *[0., 2., 0., 0.]), "Check theta_min = theta_max returns assertion error."

def test_usphere_area_assert_full_usphere():
    area = magpie.coords.usphere_area(0., 2.*np.pi, 0., np.pi)
    assert area == 4.*np.pi, "Check unit sphere area for a full sphere is 4pi."

def test_usphere_spherelonlat():
    # test forward and backwards returns the same thing.
    theta1 = np.linspace(0., np.pi, 10)
    lat = magpie.coords.sphere2lonlat(theta1)
    theta2 = magpie.coords.lonlat2sphere(lat)
    assert np.round(np.sum(theta1-theta2), decimals=4) == 0., "Forward and backward sphere to lonlat must be equal."


# test healpix.py

def test_healpix_xy2ang():
    healx = np.pi*np.array([0.1, 0.35, 1.75, 0.8, 1.])
    healy = np.pi*np.array([0.5, 0.25, 0.1, -0.4, 0.])
    phi, theta = magpie.coords.healpix_xy2ang(healx, healy)
    phi2 = np.array([0., 1.09955743, 5.49778714, 2.74889357, 3.14159265])
    theta2 = np.array([0., 0.84106867, 1.30086353, 2.81352477, 1.57079633])
    phi, phi2 = np.round(phi, decimals=5), np.round(phi2, decimals=5)
    theta, theta2 = np.round(theta, decimals=5), np.round(theta2, decimals=5)
    assert np.sum(phi2 - phi) == 0., "Check phi healpix_xy2ang."
    assert np.sum(theta2 - theta) == 0., "Check theta healpix_xy2ang."
    phi, theta = magpie.coords.healpix_xy2ang(healx[2], healy[2])
    phi, phi2 = np.round(phi, decimals=5), np.round(phi2[2], decimals=5)
    theta, theta2 = np.round(theta, decimals=5), np.round(theta2[2], decimals=5)
    assert np.sum(phi2 - phi) == 0., "Check phi healpix_xy2ang."
    assert np.sum(theta2 - theta) == 0., "Check theta healpix_xy2ang."
    # Run test on entire healpix pixel map
    nside = 16
    p = np.arange(12*nside**2)
    x, y = magpie.pixel.healpix_pix2xy(p, nside)
    phi, theta = magpie.coords.healpix_xy2ang(x, y)
    for pix in p:
        phi, theta = magpie.coords.healpix_xy2ang(x[pix], y[pix])


def test_healpix_ang2xy():
    phi = np.array([0., 1., 3./2.])*np.pi
    theta = np.array([0., 0.1, 0.75])*np.pi
    healx, healy = magpie.coords.healpix_ang2xy(phi, theta)
    healx2 = np.array([0.78539816, 3.62603832, 4.76157129])
    healy2 = np.array([ 1.57079633, 1.26984383, -0.83458047])
    healx, healx2 = np.round(healx, decimals=5), np.round(healx2, decimals=5)
    healy, healy2 = np.round(healy, decimals=5), np.round(healy2, decimals=5)
    assert np.sum(healx2 - healx) == 0., "Check healx healpix_ang2xy."
    assert np.sum(healy2 - healy) == 0., "Check healy healpix_ang2xy."
    healx, healy = magpie.coords.healpix_ang2xy(phi[2], theta[2])
    healx, healx2 = np.round(healx, decimals=5), np.round(healx2[2], decimals=5)
    healy, healy2 = np.round(healy, decimals=5), np.round(healy2[2], decimals=5)
    assert np.sum(healx2 - healx) == 0., "Check phi healpix_ang2xy."
    assert np.sum(healy2 - healy) == 0., "Check theta healpix_ang2xy."
    # Run test on entire healpix pixel map
    nside = 16
    p = np.arange(12*nside**2)
    x, y = magpie.pixel.healpix_pix2xy(p, nside)
    phi, theta = magpie.coords.healpix_xy2ang(x, y)
    x, y = magpie.coords.healpix_ang2xy(phi, theta)
    for pix in p:
        x, y = magpie.coords.healpix_ang2xy(phi[pix], theta[pix])
