===
API
===

Randoms
=======

1. Cartesian
  * :py:func:`randoms.randoms_1d(size[, xmin=0., xmax=1.])`
  * :py:func:`randoms.randoms_2d(size[, mins=[0., 0.], maxs=[1., 1.]])`
  * :py:func:`randoms.randoms_3d(size[, mins=[0., 0., 0.], maxs=[1., 1., 1.]])`
2. Polar
  * :py:func:`randoms.randoms_polar(size[, r_min=0., r_max=1., phi_min=0., phi_max=2.*np.pi])`
3. Unit Sphere
  * :py:func:`randoms.randoms_usphere(size[, phi_min=0., phi_max=2.*np.pi, theta_min=0., theta_max=np.pi])`
  * :py:func:`randoms.randoms_healpix_pixel(size, pix, nside)`
4. Spherical
  * :py:func:`randoms.random_sphere_r(size[, r_min=0., r_max=1.])`
  * :py:func:`randoms.random_sphere(size[, r_min=0., r_max=1., phi_min=0., phi_max=2*np.pi, theta_min=0., theta_max=np.pi])`
5. Sample PDF/CDF
  * :py:func:`randoms.pdf2cdf(xmid, pdf[, return_normpdf=True])`
  * :py:func:`randoms.randoms_cdf(x, cdf, size[, kind='cubic'])`
  * :py:func:`randoms.randoms_pdf(x, pdf, size[, kind='cubic'])`

Remap
=====
