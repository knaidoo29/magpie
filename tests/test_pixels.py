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
    assert check_assert(magpie.pixels.get_square, *[0., 1., 0., 1., 3])
    x, y = magpie.pixels.get_square(0., 1., 0., 1.)
    assert len(x) == len(y), "Length of x and y must match."
    assert len(x) == 40, "Length does not match input steps."
    x, y = magpie.pixels.get_square(0., 1., 0., 1., steps=16)
    assert len(x) == len(y), "Length of x and y must match."
    assert len(x) == 16, "Length does not match input steps."


def test_get_arc():
    x, y = magpie.pixels.get_arc(1., phimin=0., phimax=2.*np.pi, center=[0., 0.], steps=10)
    assert len(x) == len(y), "Length of x and y must match."
    assert len(x) == 10, "Length must match input."
    x, y = magpie.pixels.get_arc(1., phimin=0., phimax=2.*np.pi, center=[0., 0.], steps=20)
    assert len(x) == len(y), "Length of x and y must match."
    assert len(x) == 20, "Length must match input."
    x, y = magpie.pixels.get_arc(1., phimin=0., phimax=np.pi/2, center=[0., 0.], steps=10)
    x = np.round(x, decimals=4)
    y = np.round(y, decimals=4)
    assert all(x >= 0.) and all(y >= 0.), "x and y are not where they are supposed to be."
    x, y = magpie.pixels.get_arc(1., phimin=np.pi/2, phimax=np.pi, center=[0., 0.], steps=10)
    x = np.round(x, decimals=4)
    y = np.round(y, decimals=4)
    assert all(x <= 0.) and all(y >= 0.), "x and y are not where they are supposed to be."
    x, y = magpie.pixels.get_arc(1., phimin=0., phimax=2.*np.pi, center=[0., 0.], steps=10)
    r = np.round(np.sqrt(x**2 + y**2.), decimals=4)
    assert all(r == r[0]), "r should all be equivalent."
    x, y = magpie.pixels.get_arc(1., phimin=0., phimax=2.*np.pi, center=[5., 2.], steps=10)
    r = np.round(np.sqrt((x-5.)**2 + (y-2.)**2.), decimals=4)
    assert all(r == r[0]), "r should all be equivalent."


def test_get_disc():
    x, y = magpie.pixels.get_disc()
    assert len(x) == len(y), "Length of x and y must match."
    assert len(x) == 40, "Length does not match input steps."
    x, y = magpie.pixels.get_disc(steps=16)
    assert len(x) == len(y), "Length of x and y must match."
    assert len(x) == 16, "Length does not match input steps."
    x, y = magpie.pixels.get_disc(rmin=0.25, rmax=0.75)
    r = np.sqrt(x**2 + y**2)
    r = np.round(r, decimals=4)
    assert np.min(r) == 0.25, "Minimum does not match input."
    assert np.max(r) == 0.75, "Maximum does not match input."
    x, y = magpie.pixels.get_disc(rmin=0.25, rmax=0.75, center=[5., -3])
    r = np.sqrt((x-5.)**2 + (y+3)**2)
    r = np.round(r, decimals=4)
    assert np.min(r) == 0.25, "Minimum does not match input."
    assert np.max(r) == 0.75, "Maximum does not match input."
    x, y = magpie.pixels.get_disc(phimin=0., phimax=np.pi/2.)
    x = np.round(x, decimals=4)
    y = np.round(y, decimals=4)
    assert all(x >= 0) and all(y >= 0), "x and y are not where they are supposed to be."
    x, y = magpie.pixels.get_disc(phimin=np.pi/2., phimax=np.pi)
    x = np.round(x, decimals=4)
    y = np.round(y, decimals=4)
    assert all(x <= 0) and all(y >= 0), "x and y are not where they are supposed to be."


def test_get_box():
    x, y, z = magpie.pixels.get_box(0., 1., 0., 1., 0., 1.)
    assert np.shape(x) == (12, 10), "Shape of x does not match expectations."
    assert np.shape(x) == np.shape(y), "Shape of x and y must match."
    assert np.shape(y) == np.shape(z), "Shape of y and z must match."
    x, y, z = magpie.pixels.get_box(0., 1., 0., 1., 0., 1., steps=240)
    assert np.shape(x) == (12, 20), "Shape of x does not match expectations."
    assert np.shape(x) == np.shape(y), "Shape of x and y must match."
    assert np.shape(y) == np.shape(z), "Shape of y and z must match."
    assert check_assert(magpie.pixels.get_box, *[0., 1., 0., 1., 0., 1., 7])
    x, y, z = magpie.pixels.get_box(0., 1., 0., 1., 0., 1., return_nearest=True)
    assert np.shape(x) == (9, 10), "Shape of x does not match expectations."
    assert np.shape(x) == np.shape(y), "Shape of x and y must match."
    assert np.shape(y) == np.shape(z), "Shape of y and z must match."
    x, y, z = magpie.pixels.get_box(0., 1., 0., 1., 0., 1., return_nearest=True, center=[0., 2., 0.])
    assert np.shape(x) == (9, 10), "Shape of x does not match expectations."
    assert np.shape(x) == np.shape(y), "Shape of x and y must match."
    assert np.shape(y) == np.shape(z), "Shape of y and z must match."
    x, y, z = magpie.pixels.get_box(0., 1., 0., 1., 0., 1., return_nearest=True, center=[0.5, 0.5, -0.5])
    assert np.shape(x) == (4, 10), "Shape of x does not match expectations."
    assert np.shape(x) == np.shape(y), "Shape of x and y must match."
    assert np.shape(y) == np.shape(z), "Shape of y and z must match."


def test_healpix_boundary():
    # check all boundary edges run without errors
    x, y = magpie.pixels._healpix_top_left(174, 32)
    x, y = magpie.pixels._healpix_top_right(174, 32)
    x, y = magpie.pixels._healpix_bot_left(174, 32)
    x, y = magpie.pixels._healpix_bot_right(174, 32)
    x, y = magpie.pixels._healpix_top_left(174, 32, reverse=True)
    x, y = magpie.pixels._healpix_top_right(174, 32, reverse=True)
    x, y = magpie.pixels._healpix_bot_left(174, 32, reverse=True)
    x, y = magpie.pixels._healpix_bot_right(174, 32, reverse=True)
    x, y = magpie.pixels.healpix_boundary(10, 32)
    assert len(x) == 40, "Length does not match expectations."
    assert len(y) == 40, "Length does not match expectations."
    x, y = magpie.pixels.healpix_boundary(10, 32, steps=80)
    assert len(x) == 80, "Length does not match expectations."
    assert len(y) == 80, "Length does not match expectations."
    x1, y1 = magpie.pixels.healpix_boundary(982, 64, reverse=False)
    x2, y2 = magpie.pixels.healpix_boundary(982, 64, reverse=True)
    assert np.round(np.sum(x1-x2[::-1]), decimals=2) == 0., "Reversing should match."
    assert np.round(np.sum(y1-y2[::-1]), decimals=2) == 0., "Reversing should match."


def test_polar_shape():
    assert check_assert(magpie.pixels.get_polar_shape, *[np.array([0, 1, 2]), 10, 10])
    assert check_assert(magpie.pixels.get_polarEA_shape, *[np.array([0, 1, 2]), 10])
    assert check_assert(magpie.pixels.get_polar_shape, *[3, 10, 10], proj='test')
    assert check_assert(magpie.pixels.get_polarEA_shape, *[3, 10], proj='test')
    x, y = magpie.pixels.get_polar_shape(3, 10, 10, proj='cart')
    x, y = magpie.pixels.get_polarEA_shape(3, 10, proj='cart')
    x, y = magpie.pixels.get_polar_shape(3, 10, 10, proj='polar')
    x, y = magpie.pixels.get_polarEA_shape(3, 10, proj='polar')
    polygon = magpie.pixels.get_polar_shape(3, 10, 10, proj='cart', returnpoly=True)
    polygon = magpie.pixels.get_polarEA_shape(3, 10, proj='cart', returnpoly=True)
    polygon = magpie.pixels.get_polar_shape(3, 10, 10, proj='polar', returnpoly=True)
    polygon = magpie.pixels.get_polarEA_shape(3, 10, proj='polar', returnpoly=True)


def test_healpix_index():
    nside = 32
    p = np.arange(12*nside**2)
    for pix in p:
        ringi, ringj = magpie.pixels.healpix_pix2ij(pix, nside)
        _p = magpie.pixels.healpix_ij2pix(ringi, ringj, nside)
    ringi, ringj = magpie.pixels.healpix_pix2ij(p, nside)
    p2 = magpie.pixels.healpix_ij2pix(ringi, ringj, nside)
    assert np.sum(p-p2) == 0, "Test pix to ij converts forward and backward."
    idash = magpie.pixels.healpix_i2id(ringi, nside)
    for pix in p:
        jdash = magpie.pixels.healpix_j2jd(ringi[pix], ringj[pix], nside)
    jdash = magpie.pixels.healpix_j2jd(ringi, ringj, nside)
    istar, jstar = magpie.pixels.healpix_ijd2ijs(idash, jdash, nside)
    idash2, jdash2 = magpie.pixels.healpix_ijs2ijd(istar, jstar, nside)
    assert np.sum(idash - idash2) == 0, "Test pix to idash to istar converts forward and backward."
    assert np.sum(jdash - jdash2) == 0, "Test pix to jdash to jstar converts forward and backward."
    nside = 33
    p = np.arange(12*nside**2)
    for pix in p:
        ringi, ringj = magpie.pixels.healpix_pix2ij(pix, nside)
        _p = magpie.pixels.healpix_ij2pix(ringi, ringj, nside)
    ringi, ringj = magpie.pixels.healpix_pix2ij(p, nside)
    p2 = magpie.pixels.healpix_ij2pix(ringi, ringj, nside)
    assert np.sum(p-p2) == 0, "Test pix to ij converts forward and backward."
    idash = magpie.pixels.healpix_i2id(ringi, nside)
    for pix in p:
        jdash = magpie.pixels.healpix_j2jd(ringi[pix], ringj[pix], nside)
    jdash = magpie.pixels.healpix_j2jd(ringi, ringj, nside)
    istar, jstar = magpie.pixels.healpix_ijd2ijs(idash, jdash, nside)
    idash2, jdash2 = magpie.pixels.healpix_ijs2ijd(istar, jstar, nside)
    assert np.sum(idash - idash2) == 0, "Test pix to idash to istar converts forward and backward."
    assert np.sum(jdash - jdash2) == 0, "Test pix to jdash to jstar converts forward and backward."
    nside = 16
    p = np.arange(12*nside**2)
    ringi, ringj = magpie.pixels.healpix_pix2ij(p, nside)
    idash = magpie.pixels.healpix_i2id(ringi, nside)
    jdash = magpie.pixels.healpix_j2jd(ringi, ringj, nside)
    istar, jstar = magpie.pixels.healpix_ijd2ijs(idash, jdash, nside)
    # check neighbours returns without errors
    for pix in p:
        istar_neigh, jstar_neigh = magpie.pixels.healpix_ijs_neighbours(istar[pix], jstar[pix], nside)
    # check pix2xy and ij2xy returns without errors
    healx, healy = magpie.pixels.healpix_pix2xy(p, nside)


# pix2pos to pos2pix

def test_cartpixtopos():
    pixID = 10
    x, dx = magpie.pixels.pix2pos_cart1d(pixID, 100, 1000)
    pixID2 = magpie.pixels.pos2pix_cart1d(x, 100, 1000)
    assert pixID == pixID2, "pix2pos <-> pos2pix for cartesian scalar incorrect."
    pixID = np.arange(100)
    x, dx = magpie.pixels.pix2pos_cart1d(pixID, 100, 1000)
    pixID2 = magpie.pixels.pos2pix_cart1d(x, 100, 1000)
    assert all(pixID == pixID2), "pix2pos <-> pos2pix for cartesian scalar incorrect."
    # 2D
    pixID = 10
    x, y, dx, dy= magpie.pixels.pix2pos_cart2d(pixID, 100, 1000)
    pixID2 = magpie.pixels.pos2pix_cart2d(x, y, 100, 1000)
    assert pixID == pixID2, "pix2pos <-> pos2pix for cartesian scalar incorrect."
    pixID = np.arange(100)
    x, y, dx, dy = magpie.pixels.pix2pos_cart2d(pixID, 100, 1000)
    pixID2 = magpie.pixels.pos2pix_cart2d(x, y, 100, 1000)
    assert all(pixID == pixID2), "pix2pos <-> pos2pix for cartesian scalar incorrect."
    pixID = np.arange(100)
    x, y, dx, dy, xpixID, ypixID = magpie.pixels.pix2pos_cart2d(pixID, 100, 1000, return1d_pixID=True)
    pixID2 = magpie.pixels.pos2pix_cart2d(x, y, 100, 1000)
    assert all(pixID == pixID2), "pix2pos <-> pos2pix for cartesian scalar incorrect."
    pixID = 10
    x, y, dx, dy = magpie.pixels.pix2pos_cart2d(pixID, [100, 100], 1000)
    pixID2 = magpie.pixels.pos2pix_cart2d(x, y, [100, 100], 1000)
    assert pixID == pixID2, "pix2pos <-> pos2pix for cartesian scalar incorrect."
    pixID = np.arange(100)
    x, y, dx, dy = magpie.pixels.pix2pos_cart2d(pixID, [100, 100], 1000)
    pixID2 = magpie.pixels.pos2pix_cart2d(x, y, [100, 100], 1000)
    assert all(pixID == pixID2), "pix2pos <-> pos2pix for cartesian scalar incorrect."
    pixID = 10
    x, y, dx, dy = magpie.pixels.pix2pos_cart2d(pixID, 100, [1000, 1000])
    pixID2 = magpie.pixels.pos2pix_cart2d(x, y, 100, [1000, 1000])
    assert pixID == pixID2, "pix2pos <-> pos2pix for cartesian scalar incorrect."
    pixID = np.arange(100)
    x, y, dx, dy = magpie.pixels.pix2pos_cart2d(pixID, 100, [1000, 1000])
    pixID2 = magpie.pixels.pos2pix_cart2d(x, y, 100, [1000, 1000])
    assert all(pixID == pixID2), "pix2pos <-> pos2pix for cartesian scalar incorrect."
    # 3D
    pixID = 10
    x, y, z, dx, dy, dz = magpie.pixels.pix2pos_cart3d(pixID, 100, 1000)
    pixID2 = magpie.pixels.pos2pix_cart3d(x, y, z, 100, 1000)
    assert pixID == pixID2, "pix2pos <-> pos2pix for cartesian scalar incorrect."
    pixID = np.arange(100)
    x, y, z, dx, dy, dz = magpie.pixels.pix2pos_cart3d(pixID, 100, 1000)
    pixID2 = magpie.pixels.pos2pix_cart3d(x, y, z, 100, 1000)
    assert all(pixID == pixID2), "pix2pos <-> pos2pix for cartesian array incorrect."
    pixID = np.arange(100)
    x, y, z, dx, dy, dz, xpixID, ypixID, zpixID = magpie.pixels.pix2pos_cart3d(pixID, 100, 1000, return1d_pixID=True)
    pixID2 = magpie.pixels.pos2pix_cart3d(x, y, z, 100, 1000)
    assert all(pixID == pixID2), "pix2pos <-> pos2pix for cartesian array incorrect."
    pixID = 10
    x, y, z, dx, dy, dz = magpie.pixels.pix2pos_cart3d(pixID, [100, 200, 300], 1000)
    pixID2 = magpie.pixels.pos2pix_cart3d(x, y, z, [100, 200, 300], 1000)
    assert pixID == pixID2, "pix2pos <-> pos2pix for cartesian scalar incorrect."
    pixID = np.arange(100)
    x, y, z, dx, dy, dz = magpie.pixels.pix2pos_cart3d(pixID, [100, 200, 300], 1000)
    pixID2 = magpie.pixels.pos2pix_cart3d(x, y, z, [100, 200, 300], 1000)
    assert all(pixID == pixID2), "pix2pos <-> pos2pix for cartesian array incorrect."
    pixID = 10
    x, y, z, dx, dy, dz = magpie.pixels.pix2pos_cart3d(pixID, 100, [1000, 2000, 300])
    pixID2 = magpie.pixels.pos2pix_cart3d(x, y, z, 100, [1000, 2000, 300])
    assert pixID == pixID2, "pix2pos <-> pos2pix for cartesian scalar incorrect."
    pixID = np.arange(100)
    x, y, z, dx, dy, dz = magpie.pixels.pix2pos_cart3d(pixID, 100, [1000, 2000, 300])
    pixID2 = magpie.pixels.pos2pix_cart3d(x, y, z, 100, [1000, 2000, 300])
    assert all(pixID == pixID2), "pix2pos <-> pos2pix for cartesian array incorrect."
    # polar
    pixID = 10
    p, r, dp, dr = magpie.pixels.pix2pos_polar(pixID, 10, 20)
    pixID2 = magpie.pixels.pos2pix_polar(p, r, 10, 20)
    assert pixID == pixID2, "pix2pos <-> pos2pix for polar scalar incorrect."
    pixID = np.arange(100)
    p, r, dp, dr = magpie.pixels.pix2pos_polar(pixID, 10, 20)
    pixID2 = magpie.pixels.pos2pix_polar(p, r, 10, 20)
    assert all(pixID == pixID2), "pix2pos <-> pos2pix for polar array incorrect."
    # polarEA
    pixID = 10
    p, r, dp, dr = magpie.pixels.pix2pos_polarEA(pixID, 10)
    pixID2 = magpie.pixels.pos2pix_polarEA(p, r, 10)
    assert pixID == pixID2, "pix2pos <-> pos2pix for polarEA scalar incorrect."
    pixID = np.arange(100)
    p, r, dp, dr = magpie.pixels.pix2pos_polarEA(pixID, 10)
    pixID2 = magpie.pixels.pos2pix_polarEA(p, r, 10)
    assert all(pixID == pixID2), "pix2pos <-> pos2pix for polarEA array incorrect."


def test_bin_pix():
    pixID = np.arange(10)
    pix = magpie.pixels.bin_pix(pixID, 10)
    assert all(pix == 1.), "Binning not working correctly."
    weights = np.copy(pixID)
    pix = magpie.pixels.bin_pix(pixID, 10, weights=weights)
    assert np.sum(pix-weights.astype('float')) == 0., "Binning not working correctly."

def test_unique_pix():
    pixID = np.array([0, 0, 0, 2, 2, 5, 5, 5, 5])
    upixID, cpixID = magpie.pixels.get_unique_pixID(pixID)
    upixID2 = np.array([0, 2, 5])
    cpixID2 = np.array([3, 2, 4])
    assert np.sum(upixID-upixID2) == 0., "Unique pix not working correctly."
    assert np.sum(cpixID-cpixID2) == 0., "Unique pix not working correctly."
