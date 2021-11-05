Cartesian
---------


.. function:: randoms_1d(size[, xmin=0., xmax=1.])

    Returns uniform randoms in 1D.

    :param size: Number of randoms to produce.
    :type size: int
    :param xmin: Minimum value.
    :type xmin: float
    :param xmax: Maximum value.
    :type xmax: float

    :returns: **xrands** *(array)* -- Uniform randoms in 1D.


.. function:: randoms_2d(size[, mins=[0., 0.], maxs=[1., 1.]])

    Returns uniform randoms in 2D.

    :param size: Number of randoms to produce.
    :type size: int
    :param mins: Minimum values.
    :type mins: list
    :param maxs: Maximum values.
    :type maxs: list

    :returns: Returns a tuple of the following:

      * **xrands** *(array)* -- Uniform randoms in along x-axis in 2D.
      * **yrands** *(array)* -- Uniform randoms in along y-axis in 2D.


.. function:: randoms_3d(size[, mins=[0., 0., 0.], maxs=[1., 1., 1.]])

    Returns uniform randoms in 3D.

    :param size: Number of randoms to produce.
    :type size: int
    :param mins: Minimum values.
    :type mins: list
    :param maxs: Maximum values.
    :type maxs: list

    :returns: Returns a tuple of the following:

      * **xrands** *(array)* -- Uniform randoms in along x-axis in 3D.
      * **yrands** *(array)* -- Uniform randoms in along y-axis in 3D.
      * **zrands** *(array)* -- Uniform randoms in along z-axis in 3D.


Polar
-----

.. function:: randoms_polar(size[, r_min=0., r_max=1., phi_min=0., phi_max=2.*np.pi])

    Generates randoms for polar coordinates. Default will produce randoms within
    a unit circle. This can be specified to a ring segment, i.e. with inner radius
    r_min and outer radius r_max and specifying the angle of the ring segment.

    :param size: Number of randoms to produce.
    :type size: int
    :param r_min: Minimum radial value.
    :type r_min: float
    :param r_max: Maximum radial value.
    :type r_max: float
    :param phi_min: Minimum phi value.
    :type phi_min: float
    :param phi_max: Maximum phi value.
    :type phi_max: float

    :returns: Returns a tuple of the following:

      * **r** *(array)* -- Random radial coordinates.
      * **phi** *(array)* -- Random phi coordinates.


Unit Sphere
-----------


.. function:: randoms_usphere(size[, phi_min=0., phi_max=2.*np.pi, theta_min=0., theta_max=np.pi])

    Random points on the unit sphere or more generally across the surface of a sphere. The
    default will give randoms on the full sky.

    Coordinate convention:
      * phi lies in the range [0, 2pi]
      * theta lies in the rang [0, pi].

    :param size: Number of randoms to produce.
    :type size: int
    :param phi_min: Minimum phi value.
    :type phi_min: float
    :param phi_max: Maximum phi value.
    :type phi_max: float
    :param theta_min: Minimum theta value.
    :type theta_min: float
    :param theta_max: Maximum theta value.
    :type theta_max: float

    :returns: Returns a tuple of the following:

      * **phi** *(array)* -- Random phi coordinates.
      * **theta** *(array)* -- Random theta coordinates.


.. function:: randoms_healpix_pixel(size, pix, nside)

    Returns roughly `size` number of randoms inside a HEALPix pixel.

    :param size: Average number of randoms per pixel.
    :type size: int
    :param pix: Pixel identifier for healpix map.
    :type pix: int
    :param nside: Nside of the healpix map.
    :type nside: int

    :returns: Returns a tuple of the following:

      * **phi** *(array)* -- Random phi within the pixel.
      * **theta** *(array)* -- Random theta within the pixel.


Spherical
---------


.. function:: randoms_sphere_r(size[, r_min=0., r_max=1.])

    Random radial points for a segment of a sphere (default will give randoms within a unit sphere).

    :param size: Number of randoms to produce.
    :type size: int
    :param r_min: Minimum radial value.
    :type r_min: float
    :param r_max: Maximum radial value.
    :type r_max: float

    :returns: **r** *(array)* -- Random r.


.. function:: randoms_sphere(size[, r_min=0., r_max=1., phi_min=0., phi_max=2*np.pi, theta_min=0., theta_max=np.pi])

    Random points inside a sphere (default will give randoms within a unit sphere).
    You can specify the inner and outer radii to get randoms in a shell and the region
    on the sky.

    Coordinate convention:
      * phi lies in the range [0, 2pi]
      * theta lies in the rang [0, pi].

    :param size: Number of randoms to produce.
    :type size: int
    :param r_min: Minimum radial value.
    :type r_min: float
    :param r_max: Maximum radial value.
    :type r_max: float
    :param phi_min: Minimum phi value.
    :type phi_min: float
    :param phi_max: Maximum phi value.
    :type phi_max: float
    :param theta_min: Minimum theta value.
    :type theta_min: float
    :param theta_max: Maximum theta value.
    :type theta_max: float

    :returns: Returns a tuple of the following:

      * **r** *(array)* -- Random r.
      * **phi** *(array)* -- Random phi coordinates.
      * **theta** *(array)* -- Random theta coordinates.


Sample PDF/CDF Functions
------------------------


.. function:: pdf2cdf(xmid, pdf[, return_normpdf=True])

    Calculates the CDF from a given PDF.

    :param xmid: Linearly spaced x-values given at the middle of a bin of length dx.
    :type xmid: array
    :param pdf: Probabilty distribution function.
    :type pdf: array
    :param return_normpdf: Normalise PDF is also outputed.
    :type return_normpdf: bool

    :returns: Returns a tuple of the following:

        * **x** *(array)* -- X-coordinates.
        * **cdf** *(array)* -- Cumulative distribution function with extreme points set 0 and 1.
        * **normpdf** *(array)* -- Normalised PDF.


.. function:: randoms_cdf(x, cdf, size[, kind='cubic'])

    Generates randoms from a given cumulative distribution function.

    :param x: X-coordinates.
    :type x: array
    :param cdf: Cumulative distribution function, extreme points must be 0 and 1 i.e. cdf[0] = 0 and cdf[-1] = 1.
    :type cdf: array
    :param size: Size of the random sample.
    :type size: int
    :param kind: Scipy CDF interpolation kind.
    :type kind: str

    :returns: **rands** *(array)* -- Randoms drawn from sample CDF.


.. function:: randoms_pdf(x, pdf, size[, kind='cubic'])

    Generates randoms from a given probability distribution function by first calculating a CDF.

    :param xmid: Linearly spaced x-values given at the middle of a bin of length dx.
    :type xmid: array
    :param pdf: Probabilty distribution function.
    :type pdf: array
    :param size: Size of the random sample.
    :type size: int
    :param kind: Scipy CDF interpolation kind.
    :type kind: str

    :returns: **rands** *(array)* -- Randoms drawn from sample PDF.
