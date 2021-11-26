import numpy as np
import magpie


# AssertionError function

def check_assert(function, *args, **kwargs):
    """Check AssertionError in functions."""
    try:
        function(*args, **kwargs)
    except AssertionError:
        return True


# Basic shapes

def test_get_square():
    assert check_assert(magpie.pixel.get_square, *[0., 1., 0., 1., 3])
    x, y = magpie.pixel.get_square(0., 1., 0., 1.)
    assert len(x) == len(y), "Length of x and y must match."
    assert len(x) == 40, "Length does not match input steps."
    x, y = magpie.pixel.get_square(0., 1., 0., 1., steps=16)
    assert len(x) == len(y), "Length of x and y must match."
    assert len(x) == 16, "Length does not match input steps."


def test_get_arc():
    x, y = magpie.pixel.get_arc(1., phimin=0., phimax=2.*np.pi, center=[0., 0.], steps=10)
    assert len(x) == len(y), "Length of x and y must match."
    assert len(x) == 10, "Length must match input."
    x, y = magpie.pixel.get_arc(1., phimin=0., phimax=2.*np.pi, center=[0., 0.], steps=20)
    assert len(x) == len(y), "Length of x and y must match."
    assert len(x) == 20, "Length must match input."
    x, y = magpie.pixel.get_arc(1., phimin=0., phimax=np.pi/2, center=[0., 0.], steps=10)
    x = np.round(x, decimals=4)
    y = np.round(y, decimals=4)
    assert all(x >= 0.) and all(y >= 0.), "x and y are not where they are supposed to be."
    x, y = magpie.pixel.get_arc(1., phimin=np.pi/2, phimax=np.pi, center=[0., 0.], steps=10)
    x = np.round(x, decimals=4)
    y = np.round(y, decimals=4)
    assert all(x <= 0.) and all(y >= 0.), "x and y are not where they are supposed to be."
    x, y = magpie.pixel.get_arc(1., phimin=0., phimax=2.*np.pi, center=[0., 0.], steps=10)
    r = np.round(np.sqrt(x**2 + y**2.), decimals=4)
    assert all(r == r[0]), "r should all be equivalent."
    x, y = magpie.pixel.get_arc(1., phimin=0., phimax=2.*np.pi, center=[5., 2.], steps=10)
    r = np.round(np.sqrt((x-5.)**2 + (y-2.)**2.), decimals=4)
    assert all(r == r[0]), "r should all be equivalent."


def test_get_disc():
    x, y = magpie.pixel.get_disc()
    assert len(x) == len(y), "Length of x and y must match."
    assert len(x) == 40, "Length does not match input steps."
    x, y = magpie.pixel.get_disc(steps=16)
    assert len(x) == len(y), "Length of x and y must match."
    assert len(x) == 16, "Length does not match input steps."
    x, y = magpie.pixel.get_disc(rmin=0.25, rmax=0.75)
    r = np.sqrt(x**2 + y**2)
    r = np.round(r, decimals=4)
    assert np.min(r) == 0.25, "Minimum does not match input."
    assert np.max(r) == 0.75, "Maximum does not match input."
    x, y = magpie.pixel.get_disc(rmin=0.25, rmax=0.75, center=[5., -3])
    r = np.sqrt((x-5.)**2 + (y+3)**2)
    r = np.round(r, decimals=4)
    assert np.min(r) == 0.25, "Minimum does not match input."
    assert np.max(r) == 0.75, "Maximum does not match input."
    x, y = magpie.pixel.get_disc(phimin=0., phimax=np.pi/2.)
    x = np.round(x, decimals=4)
    y = np.round(y, decimals=4)
    assert all(x >= 0) and all(y >= 0), "x and y are not where they are supposed to be."
    x, y = magpie.pixel.get_disc(phimin=np.pi/2., phimax=np.pi)
    x = np.round(x, decimals=4)
    y = np.round(y, decimals=4)
    assert all(x <= 0) and all(y >= 0), "x and y are not where they are supposed to be."


def test_get_box():
    x, y, z = magpie.pixel.get_box(0., 1., 0., 1., 0., 1.)
    assert np.shape(x) == (12, 10), "Shape of x does not match expectations."
    assert np.shape(x) == np.shape(y), "Shape of x and y must match."
    assert np.shape(y) == np.shape(z), "Shape of y and z must match."
    x, y, z = magpie.pixel.get_box(0., 1., 0., 1., 0., 1., steps=240)
    assert np.shape(x) == (12, 20), "Shape of x does not match expectations."
    assert np.shape(x) == np.shape(y), "Shape of x and y must match."
    assert np.shape(y) == np.shape(z), "Shape of y and z must match."
    assert check_assert(magpie.pixel.get_box, *[0., 1., 0., 1., 0., 1., 7])
    x, y, z = magpie.pixel.get_box(0., 1., 0., 1., 0., 1., return_nearest=True)
    assert np.shape(x) == (9, 10), "Shape of x does not match expectations."
    assert np.shape(x) == np.shape(y), "Shape of x and y must match."
    assert np.shape(y) == np.shape(z), "Shape of y and z must match."
    x, y, z = magpie.pixel.get_box(0., 1., 0., 1., 0., 1., return_nearest=True, center=[0., 2., 0.])
    assert np.shape(x) == (9, 10), "Shape of x does not match expectations."
    assert np.shape(x) == np.shape(y), "Shape of x and y must match."
    assert np.shape(y) == np.shape(z), "Shape of y and z must match."
    x, y, z = magpie.pixel.get_box(0., 1., 0., 1., 0., 1., return_nearest=True, center=[0.5, 0.5, -0.5])
    assert np.shape(x) == (4, 10), "Shape of x does not match expectations."
    assert np.shape(x) == np.shape(y), "Shape of x and y must match."
    assert np.shape(y) == np.shape(z), "Shape of y and z must match."


def test_healpix_boundary():
    x, y = magpie.pixel.healpix_boundary(10, 32)
    assert len(x) == 40, "Length does not match expectations."
    assert len(y) == 40, "Length does not match expectations."
    x, y = magpie.pixel.healpix_boundary(10, 32, steps=80)
    assert len(x) == 80, "Length does not match expectations."
    assert len(y) == 80, "Length does not match expectations."
    x1, y1 = magpie.pixel.healpix_boundary(982, 64, reverse=False)
    x2, y2 = magpie.pixel.healpix_boundary(982, 64, reverse=True)
    assert np.round(np.sum(x1-x2[::-1]), decimals=2) == 0., "Reversing should match."
    assert np.round(np.sum(y1-y2[::-1]), decimals=2) == 0., "Reversing should match."
