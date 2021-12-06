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

# test distance.py

def test_dist():

    x1, x2 = 1., 4.
    dist = magpie.coords.dist1d(x1, x2)
    assert dist == 3., "dist1d working incorrectly."
    x1, x2 = 1.*np.arange(10), 4.*np.arange(10)
    dist = magpie.coords.dist1d(x1, x2)
    assert np.sum(dist-abs(x2-x1)) == 0., "dist1d working incorrectly."

    x1, y1, x2, y2 = 1., 1., 4., 1.
    dist = magpie.coords.dist2d(x1, y1, x2, y2)
    assert dist == 3., "dist2d working incorrectly."
    x1, y1, x2, y2 = 1., 1., 1., 4.
    dist = magpie.coords.dist2d(x1, y1, x2, y2)
    assert dist == 3., "dist2d working incorrectly."
    x1, y1, x2, y2 = 1.*np.arange(10), 4.*np.arange(10), 5.*np.arange(10), 6.*np.arange(10)
    dist = magpie.coords.dist2d(x1, y1, x2, y2)
    assert np.sum(dist-np.sqrt((x2-x1)**2 + (y2-y1)**2)) == 0., "dist2d working incorrectly."

    x1, y1, z1, x2, y2, z2 = 1., 1., 1., 4., 1., 1.
    dist = magpie.coords.dist3d(x1, y1, z1, x2, y2, z2)
    assert dist == 3., "dist3d working incorrectly."
    x1, y1, z1, x2, y2, z2 = 1., 1., 1., 1., 1., 4.
    dist = magpie.coords.dist3d(x1, y1, z1, x2, y2, z2)
    assert dist == 3., "dist3d working incorrectly."
    x1, y1, z1, x2, y2, z2 = 1.*np.arange(10), 4.*np.arange(10), 5.*np.arange(10), 6.*np.arange(10), -5.*np.arange(10), -6.*np.arange(10)
    dist = magpie.coords.dist3d(x1, y1, z1, x2, y2, z2)
    assert np.sum(dist-np.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)) == 0., "dist3d working incorrectly."

    p1, t1, p2, t2 = 0., 0., 0., np.pi/2.
    dist = magpie.coords.distusphere(p1, t1, p2, t2)
    assert dist == np.pi/2., "distusphere working incorrectly."
    p1, t1, p2, t2 = np.pi/2., np.pi/2., 3.*np.pi/2., np.pi/2.
    dist = magpie.coords.distusphere(p1, t1, p2, t2)
    assert dist == np.pi, "distusphere working incorrectly."
    p1, t1 = np.linspace(0., np.pi, 100), 0.2*np.pi*np.ones(100)
    p2, t2 = np.zeros(100), np.zeros(100)
    dist = magpie.coords.distusphere(p1, t1, p2, t2)
    assert all(dist == 0.2*np.pi), "distusphere working incorrectly"

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
    x, y = magpie.pixels.healpix_pix2xy(p, nside)
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
    x, y = magpie.pixels.healpix_pix2xy(p, nside)
    phi, theta = magpie.coords.healpix_xy2ang(x, y)
    x, y = magpie.coords.healpix_ang2xy(phi, theta)
    for pix in p:
        x, y = magpie.coords.healpix_ang2xy(phi[pix], theta[pix])


# test rotations

def test_rotate2d():
    x, y = 1., 0.
    xrot, yrot = magpie.coords.rotate2d(x, y, np.deg2rad(90.))
    xrot = np.round(xrot, decimals=4)
    yrot = np.round(yrot, decimals=4)
    assert xrot == 0. and yrot == 1., "rotate2d not behaving as expected."
    x, y = np.array([1., 0., -1., 0.]), np.array([0., 1., 0., -1])
    xexp, yexp = np.array([0., -1., 0., 1.]), np.array([1., 0., -1., 0.])
    xrot, yrot = magpie.coords.rotate2d(x, y, np.deg2rad(90.))
    xrot = np.round(xrot, decimals=4)
    yrot = np.round(yrot, decimals=4)
    assert np.sum(abs(xrot-xexp)) == 0. and np.sum(abs(yrot-yexp)) == 0., "rotate2d not behaving as expected."
    x, y = 1., 0.
    center = [1., 1.]
    xrot, yrot = magpie.coords.rotate2d(x, y, np.deg2rad(90.), center=center)
    xrot = np.round(xrot, decimals=4)
    yrot = np.round(yrot, decimals=4)
    assert xrot == 2. and yrot == 1., "rotate2d not behaving as expected."
    x, y = np.array([1., 0., -1., 0.]), np.array([0., 1., 0., -1])
    xexp, yexp = np.array([2., 1., 2., 3.]), np.array([1., 0., -1., 0.])
    xrot, yrot = magpie.coords.rotate2d(x, y, np.deg2rad(90.), center = [1., 1.])
    xrot = np.round(xrot, decimals=4)
    yrot = np.round(yrot, decimals=4)
    assert np.sum(abs(xrot-xexp)) == 0. and np.sum(abs(yrot-yexp))  == 0., "rotate2d not behaving as expected."

def test_rotate3d_Euler():
    x, y, z = 1., 0., 0.
    xrot, yrot, zrot = magpie.coords.rotate3d_Euler(x, y, z, np.deg2rad([90., 0., 0.]), axes='zyz')
    xrot = np.round(xrot, decimals=4)
    yrot = np.round(yrot, decimals=4)
    zrot = np.round(zrot, decimals=4)
    assert xrot == 0. and yrot == 1. and zrot == 0., "rotate3d_Euler not behaving as expected."
    x, y, z = np.array([1., 0., -1., 0.]), np.array([0., 1., 0., -1]), np.array([0., 0., 0., 0.])
    xexp, yexp, zexp = np.array([0., -1., 0., 1.]), np.array([1., 0., -1., 0.]), np.array([0., 0., 0., 0.])
    xrot, yrot, zrot = magpie.coords.rotate3d_Euler(x, y, z, np.deg2rad([90., 0., 0.]), axes='zyz')
    xrot = np.round(xrot, decimals=4)
    yrot = np.round(yrot, decimals=4)
    zrot = np.round(zrot, decimals=4)
    assert np.sum(abs(xrot-xexp)) == 0. and np.sum(abs(yrot-yexp)) == 0. and np.sum(abs(zrot-zexp)) == 0., "rotate3d_Euler not behaving as expected."
    x, y, z = 0., 1., 0.
    xrot, yrot, zrot = magpie.coords.rotate3d_Euler(x, y, z, np.deg2rad([90., 0., 0.]), axes='zyz')
    xrot = np.round(xrot, decimals=4)
    yrot = np.round(yrot, decimals=4)
    zrot = np.round(zrot, decimals=4)
    assert xrot == -1. and yrot == 0. and zrot == 0., "rotate3d_Euler not behaving as expected."
    x, y, z = np.array([1., 0., -1., 0.]), np.array([0., 0., 0., 0.]), np.array([0., 1., 0., -1])
    xexp, yexp, zexp = np.array([0., 0., 0., 0.]), np.array([1., 0., -1., 0.]), np.array([0., 1., 0., -1.])
    xrot, yrot, zrot = magpie.coords.rotate3d_Euler(x, y, z, np.deg2rad([90., 0., 0.]), axes='zyz')
    xrot = np.round(xrot, decimals=4)
    yrot = np.round(yrot, decimals=4)
    zrot = np.round(zrot, decimals=4)
    assert np.sum(abs(xrot-xexp)) == 0. and np.sum(abs(yrot-yexp)) == 0. and np.sum(abs(zrot-zexp)) == 0., "rotate3d_Euler not behaving as expected."
    x = np.array([1., 0.25, 5.])
    y = np.array([0.75, 4., 2.])
    z = np.array([3., 4., 2.])
    xexp = np.array([0.5477, -1.2369, -2.385])
    yexp = np.array([2.3028, 1.8978, 5.1529])
    zexp = np.array([2.227, 5.1895, 0.8712])
    xrot, yrot, zrot = magpie.coords.rotate3d_Euler(x, y, z, np.deg2rad([60., 45., 45.]), axes='zyz')
    xrot = np.round(xrot, decimals=4)
    yrot = np.round(yrot, decimals=4)
    zrot = np.round(zrot, decimals=4)
    assert np.sum(abs(xrot-xexp)) == 0. and np.sum(abs(yrot-yexp)) == 0. and np.sum(abs(zrot-zexp)) == 0., "rotate3d_Euler not behaving as expected."
    xexp = np.array([3.1467, 3.8923, 4.3837])
    yexp = np.array([0.0028, 1.8218, 3.3484])
    zexp = np.array([0.8128, 3.6869, -1.6037])
    xrot, yrot, zrot = magpie.coords.rotate3d_Euler(x, y, z, np.deg2rad([60., 45., 45.]), axes='xyz')
    xrot = np.round(xrot, decimals=4)
    yrot = np.round(yrot, decimals=4)
    zrot = np.round(zrot, decimals=4)
    assert np.sum(abs(xrot-xexp)) == 0. and np.sum(abs(yrot-yexp)) == 0. and np.sum(abs(zrot-zexp)) == 0., "rotate3d_Euler not behaving as expected."


def test_rotate3d_Rodrigues():
    x, y, z = 1., 0., 0.
    xrot, yrot, zrot = magpie.coords.rotate3d_Euler(x, y, z, np.deg2rad([90., 0., 0.]), axes='zyz')
    xrot2, yrot2, zrot2 = magpie.coords.rotate3d_Rodrigues(x, y, z, np.array([0., 0., 1.]), np.deg2rad(90.))
    xrot = np.round(xrot, decimals=4)
    yrot = np.round(yrot, decimals=4)
    zrot = np.round(zrot, decimals=4)
    xrot2 = np.round(xrot2, decimals=4)
    yrot2 = np.round(yrot2, decimals=4)
    zrot2 = np.round(zrot2, decimals=4)
    assert xrot-xrot2 == 0. and yrot-yrot2 == 0. and zrot-zrot2 == 0., "rotate3d_Rodrigues not behaving as expected."
    x = np.array([1., 0.25, 5.])
    y = np.array([0.75, 4., 2.])
    z = np.array([3., 4., 2.])
    xexp = np.array([0.5477, -1.2369, -2.385])
    yexp = np.array([2.3028, 1.8978, 5.1529])
    zexp = np.array([2.227, 5.1895, 0.8712])
    xrot, yrot, zrot = magpie.coords.rotate3d_Euler(x, y, z, np.deg2rad([60., 0., 0.]), axes='xxx')
    xrot2, yrot2, zrot2 = magpie.coords.rotate3d_Rodrigues(x, y, z, np.array([1., 0., 0.]), np.deg2rad(60.))
    xrot = np.round(xrot, decimals=4)
    yrot = np.round(yrot, decimals=4)
    zrot = np.round(zrot, decimals=4)
    xrot2 = np.round(xrot2, decimals=4)
    yrot2 = np.round(yrot2, decimals=4)
    zrot2 = np.round(zrot2, decimals=4)
    assert np.sum(abs(xrot-xrot2)) == 0. and np.sum(abs(yrot-yrot2)) == 0. and np.sum(abs(zrot-zrot2)) == 0., \
        "rotate3d_Rodrigues not behaving as expected."
    xrot2, yrot2, zrot2 = magpie.coords.rotate3d_Rodrigues(x, y, z, np.array([3., 0., 0.]), np.deg2rad(60.))
    xrot = np.round(xrot, decimals=4)
    yrot = np.round(yrot, decimals=4)
    zrot = np.round(zrot, decimals=4)
    xrot2 = np.round(xrot2, decimals=4)
    yrot2 = np.round(yrot2, decimals=4)
    zrot2 = np.round(zrot2, decimals=4)
    assert np.sum(abs(xrot-xrot2)) == 0. and np.sum(abs(yrot-yrot2)) == 0. and np.sum(abs(zrot-zrot2)) == 0., \
        "rotate3d_Rodrigues not behaving as expected."
