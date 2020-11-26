import numpy as np
import magpie


# AssertionError function

def check_assert(function, *args, **kwargs):
    """Check AssertionError in functions."""
    try:
        function(*args, **kwargs)
    except AssertionError:
        return True


# Test sky_util.py

def test_sky_area_assert_phi_min_less_zero():
    assert check_assert(magpie.coords.sky_area, *[-0.1, 2., 0., 2.]), "Check phi_min < 0. returns assertion error."

def test_sky_area_assert_phi_min_more_2pi():
    assert check_assert(magpie.coords.sky_area, *[2.*np.pi+0.1, 2., 0., 2.]), "Check phi_min > 2pi returns assertion error."

def test_sky_area_assert_phi_max_less_zero():
    assert check_assert(magpie.coords.sky_area, *[0., -0.1, 0., 2.]), "Check phi_max < 0. returns assertion error."

def test_sky_area_assert_phi_max_more_2pi():
    assert check_assert(magpie.coords.sky_area, *[0., 2.*np.pi+0.1, 0., 2.]), "Check phi_max > 2pi returns assertion error."

def test_sky_area_assert_phi_min_equals_phi_max():
    assert check_assert(magpie.coords.sky_area, *[0., 0., 0., 2.]), "Check phi_min = phi_max returns assertion error."

def test_sky_area_assert_theta_min_less_zero():
    assert check_assert(magpie.coords.sky_area, *[0., 2., -0.1, 2.]), "Check theta_min < 0. returns assertion error."

def test_sky_area_assert_theta_min_more_pi():
    assert check_assert(magpie.coords.sky_area, *[0., 2., np.pi+0.1, 2.]), "Check theta_min > pi returns assertion error."

def test_sky_area_assert_theta_max_less_zero():
    assert check_assert(magpie.coords.sky_area, *[0., 2., -0.1, 2.]), "Check theta_max < 0. returns assertion error."

def test_sky_area_assert_theta_max_more_2pi():
    assert check_assert(magpie.coords.sky_area, *[0., 2., np.pi+0.1, 2.]), "Check theta_max > 2pi returns assertion error."

def test_sky_area_assert_theta_min_equals_theta_max():
    assert check_assert(magpie.coords.sky_area, *[0., 2., 0., 0.]), "Check theta_min = theta_max returns assertion error."

def test_sky_area_assert_full_sky():
    area = magpie.coords.sky_area(0., 2.*np.pi, 0., np.pi)
    assert area == 4.*np.pi, "Check sky area full sky area is 4pi."


# test transform.py

def test_cart2polar():
    # check scalar case
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
