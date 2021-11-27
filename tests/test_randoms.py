import numpy as np
import healpy as hp
import magpie


def test_randoms_1d():
    xrands = magpie.randoms.randoms_1d(100)
    cond = np.where((xrands >= 0.) & (xrands <= 1.))[0]
    assert len(cond) == 100, "Check randoms are in the right range."
    xrands = magpie.randoms.randoms_1d(100, xmin=0.25)
    cond = np.where((xrands >= 0.25) & (xrands <= 1.))[0]
    assert len(cond) == 100, "Check randoms are in the right range."
    xrands = magpie.randoms.randoms_1d(100, xmin=0., xmax=0.75)
    cond = np.where((xrands >= 0.) & (xrands <= 0.75))[0]
    assert len(cond) == 100, "Check randoms are in the right range."
    xrands = magpie.randoms.randoms_1d(100, xmin=10., xmax=15.)
    cond = np.where((xrands >= 10.) & (xrands <= 15.))[0]
    assert len(cond) == 100, "Check randoms are in the right range."


def test_randoms_2d():
    xrands, yrands = magpie.randoms.randoms_2d(100)
    cond = np.where((xrands >= 0.) & (xrands <= 1.) & (yrands >= 0.) & (yrands <= 1.))[0]
    assert len(cond) == 100, "Check randoms are in the right range."
    xrands, yrands = magpie.randoms.randoms_2d(100, mins=[0.5, 0.25])
    cond = np.where((xrands >= 0.5) & (xrands <= 1.) & (yrands >= 0.25) & (yrands <= 1.))[0]
    assert len(cond) == 100, "Check randoms are in the right range."
    xrands, yrands = magpie.randoms.randoms_2d(100, maxs=[0.5, 0.75])
    cond = np.where((xrands >= 0.) & (xrands <= 0.5) & (yrands >= 0.) & (yrands <= 0.75))[0]
    assert len(cond) == 100, "Check randoms are in the right range."
    xrands, yrands = magpie.randoms.randoms_2d(100, mins=[10, 20], maxs=[20, 30])
    cond = np.where((xrands >= 10) & (xrands <= 20) & (yrands >= 20) & (yrands <= 30))[0]
    assert len(cond) == 100, "Check randoms are in the right range."


def test_randoms_3d():
    xrands, yrands, zrands = magpie.randoms.randoms_3d(100)
    cond = np.where((xrands >= 0.) & (xrands <= 1.) & (yrands >= 0.) & (yrands <= 1.) & (zrands >= 0.) & (zrands <= 1.))[0]
    assert len(cond) == 100, "Check randoms are in the right range."
    xrands, yrands, zrands = magpie.randoms.randoms_3d(100, mins=[0.1, 0.5, 0.25])
    cond = np.where((xrands >= 0.1) & (xrands <= 1.) & (yrands >= 0.5) & (yrands <= 1.) & (zrands >= 0.25) & (zrands <= 1.))[0]
    assert len(cond) == 100, "Check randoms are in the right range."
    xrands, yrands, zrands = magpie.randoms.randoms_3d(100, maxs=[0.5, 0.75, 0.8])
    cond = np.where((xrands >= 0.) & (xrands <= 0.5) & (yrands >= 0.) & (yrands <= 0.75) & (zrands >= 0.) & (zrands <= 0.8))[0]
    assert len(cond) == 100, "Check randoms are in the right range."
    xrands, yrands, zrands = magpie.randoms.randoms_3d(100, mins=[-10, 20, 40], maxs=[-5, 50, 60])
    cond = np.where((xrands >= -10.) & (xrands <= -5.) & (yrands >= 20.) & (yrands <= 50.) & (zrands >= 40.) & (zrands <= 60.))[0]
    assert len(cond) == 100, "Check randoms are in the right range."


def test_pdf_functions():
    xedges = magpie.grids.get_xedges(10., 10)
    xmid = magpie.grids.xedges2mid(xedges)
    pdf = np.ones(len(xmid))
    pdf[-5:] = 0.
    x, cdf, normpdf = magpie.randoms.pdf2cdf(xmid, pdf)
    assert normpdf[0] == 0.2, "norm pdf is incorrect."
    assert cdf[-6] == 1., "cdf is incorrect."
    x, cdf = magpie.randoms.pdf2cdf(xmid, pdf, return_normpdf=False)
    rands = magpie.randoms.randoms_cdf(x[:6], cdf[:6], 100)
    cond = np.where((rands >= 0) & (rands <= 5.))[0]
    assert len(cond) == 100, "cdf randoms not behaving as expected."
    rands = magpie.randoms.randoms_pdf(xmid[:5], pdf[:5], 100)
    cond = np.where((rands >= 0) & (rands <= 5.))[0]
    assert len(cond) == 100, "pdf randoms not behaving as expected."


def test_randoms_polar():
    r, phi = magpie.randoms.randoms_polar(100)
    cond = np.where((r >= 0.) & (r <= 1.) & (phi >= 0.) & (phi <= 2.*np.pi))[0]
    assert len(cond) == 100, "Check randoms are in the right range."
    r, phi = magpie.randoms.randoms_polar(100, r_min=0.5)
    cond = np.where((r >= 0.5) & (r <= 1.) & (phi >= 0.) & (phi <= 2.*np.pi))[0]
    assert len(cond) == 100, "Check randoms are in the right range."
    r, phi = magpie.randoms.randoms_polar(100, r_max=0.5)
    cond = np.where((r >= 0.) & (r <= 0.5) & (phi >= 0.) & (phi <= 2.*np.pi))[0]
    assert len(cond) == 100, "Check randoms are in the right range."
    r, phi = magpie.randoms.randoms_polar(100, phi_min=1.)
    cond = np.where((r >= 0.) & (r <= 1.) & (phi >= 1.) & (phi <= 2.*np.pi))[0]
    assert len(cond) == 100, "Check randoms are in the right range."
    r, phi = magpie.randoms.randoms_polar(100, phi_max=2.5)
    cond = np.where((r >= 0.) & (r <= 1.) & (phi >= 0.) & (phi <= 2.5))[0]
    assert len(cond) == 100, "Check randoms are in the right range."
    r, phi = magpie.randoms.randoms_polar(100, r_min=0.7, r_max=0.9, phi_min=0.25, phi_max=2.5)
    cond = np.where((r >= 0.7) & (r <= 0.9) & (phi >= 0.25) & (phi <= 2.5))[0]
    assert len(cond) == 100, "Check randoms are in the right range."


def test_randoms_sphere_r():
    r = magpie.randoms.randoms_sphere_r(100)
    cond = np.where((r >= 0.) & (r <= 1.))[0]
    assert len(cond) == 100, "Check randoms are in the right range."
    r = magpie.randoms.randoms_sphere_r(100, r_min=0.5)
    cond = np.where((r >= 0.5) & (r <= 1.))[0]
    assert len(cond) == 100, "Check randoms are in the right range."
    r = magpie.randoms.randoms_sphere_r(100, r_max=0.5)
    cond = np.where((r >= 0.) & (r <= 0.5))[0]
    assert len(cond) == 100, "Check randoms are in the right range."


def test_randoms_sphere():
    r, phi, theta = magpie.randoms.randoms_sphere(100, r_min=0., r_max=1., phi_min=0., phi_max=2*np.pi,
                                                  theta_min=0., theta_max=np.pi)
    cond = np.where((r >= 0.) & (r <= 1.) & (phi >= 0.) & (phi <= 2.*np.pi) & (theta >= 0.) & (theta <= np.pi))[0]
    r, phi, theta = magpie.randoms.randoms_sphere(100, r_min=0.5, r_max=1., phi_min=0., phi_max=2*np.pi,
                                                  theta_min=0., theta_max=np.pi)
    cond = np.where((r >= 0.5) & (r <= 1.) & (phi >= 0.) & (phi <= 2.*np.pi) & (theta >= 0.) & (theta <= np.pi))[0]
    r, phi, theta = magpie.randoms.randoms_sphere(100, r_min=0., r_max=0.5, phi_min=0., phi_max=2*np.pi,
                                                  theta_min=0., theta_max=np.pi)
    cond = np.where((r >= 0.) & (r <= 0.5) & (phi >= 0.) & (phi <= 2.*np.pi) & (theta >= 0.) & (theta <= np.pi))[0]
    r, phi, theta = magpie.randoms.randoms_sphere(100, r_min=0., r_max=1., phi_min=np.pi, phi_max=2*np.pi,
                                                  theta_min=0., theta_max=np.pi)
    cond = np.where((r >= 0.) & (r <= 1.) & (phi >= np.pi) & (phi <= 2.*np.pi) & (theta >= 0.) & (theta <= np.pi))[0]
    r, phi, theta = magpie.randoms.randoms_sphere(100, r_min=0.5, r_max=1., phi_min=0., phi_max=np.pi,
                                                  theta_min=0., theta_max=np.pi)
    cond = np.where((r >= 0.) & (r <= 1.) & (phi >= 0.) & (phi <= np.pi) & (theta >= 0.) & (theta <= np.pi))[0]
    r, phi, theta = magpie.randoms.randoms_sphere(100, r_min=0., r_max=1., phi_min=0., phi_max=2*np.pi,
                                                  theta_min=np.pi/2, theta_max=np.pi)
    cond = np.where((r >= 0.) & (r <= 1.) & (phi >= 0.) & (phi <= 2.*np.pi) & (theta >= np.pi/2) & (theta <= np.pi))[0]
    r, phi, theta = magpie.randoms.randoms_sphere(100, r_min=0., r_max=1., phi_min=0., phi_max=2*np.pi,
                                                  theta_min=0., theta_max=np.pi/2)
    cond = np.where((r >= 0.) & (r <= 1.) & (phi >= 0.) & (phi <= 2.*np.pi) & (theta >= 0.) & (theta <= np.pi/2))[0]
    r, phi, theta = magpie.randoms.randoms_sphere(100, r_min=10., r_max=15., phi_min=3, phi_max=5,
                                                  theta_min=1.25, theta_max=2.10)
    cond = np.where((r >= 10.) & (r <= 15.) & (phi >= 3) & (phi <= 5) & (theta >= 1.25) & (theta <= 2.10))[0]



def test_randoms_usphere():
    phi, theta = magpie.randoms.randoms_usphere(100, phi_min=0., phi_max=2*np.pi, theta_min=0., theta_max=np.pi)
    cond = np.where((phi >= 0.) & (phi <= 2.*np.pi) & (theta >= 0.) & (theta <= np.pi))[0]
    phi, theta = magpie.randoms.randoms_usphere(100, phi_min=np.pi, phi_max=2*np.pi, theta_min=0., theta_max=np.pi)
    cond = np.where((phi >= np.pi) & (phi <= 2.*np.pi) & (theta >= 0.) & (theta <= np.pi))[0]
    phi, theta = magpie.randoms.randoms_usphere(100, phi_min=0., phi_max=np.pi, theta_min=0., theta_max=np.pi)
    cond = np.where((phi >= 0.) & (phi <= np.pi) & (theta >= 0.) & (theta <= np.pi))[0]
    phi, theta = magpie.randoms.randoms_usphere(100, phi_min=0., phi_max=2*np.pi, theta_min=np.pi/2, theta_max=np.pi)
    cond = np.where((phi >= 0.) & (phi <= 2.*np.pi) & (theta >= np.pi/2) & (theta <= np.pi))[0]
    phi, theta = magpie.randoms.randoms_usphere(100, phi_min=0., phi_max=2*np.pi, theta_min=0., theta_max=np.pi/2)
    cond = np.where((phi >= 0.) & (phi <= 2.*np.pi) & (theta >= 0.) & (theta <= np.pi/2))[0]
    phi, theta = magpie.randoms.randoms_usphere(100, phi_min=3, phi_max=5, theta_min=1.25, theta_max=2.10)
    cond = np.where((phi >= 3) & (phi <= 5) & (theta >= 1.25) & (theta <= 2.10))[0]


def test_randoms_healpix_pixel():
    nside = 4
    p = np.arange(12*nside**2)
    for pix in p:
        phi, theta = magpie.randoms.randoms_healpix_pixel(10, pix, nside)
        ind = hp.ang2pix(nside, theta, phi)
        assert all(ind == ind[0]), "Healpix randoms are not correct."
