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

## CONTINUE FROM POLAR2CART
