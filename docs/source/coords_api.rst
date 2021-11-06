
Conversions
-----------


.. function:: coords.cart2polar(x, y[, center=[0., 0.]])

    Returns the polar coordinates for a given set of cartesian coordinates.

    :param x: x coordinates.
    :type x: array
    :param y: y coordinates.
    :type y: array
    :param center: Center point of polar coordinate grid.
    :type center: list

    :returns:
      * **r** *(array)* -- Radial coordinates.
      * **phi** *(array)* -- Phi coordinates.


.. function:: coords.polar2cart(r, p[, center=[0., 0.]])

    Returns the polar coordinates for a given set of cartesian coordinates.

    :param r: Radial coordinates.
    :type r: array
    :param p: Phi coordinates.
    :type p: array
    :param center: Center point of polar coordinate grid.
    :type center: list

    :returns:
      * **x** *(array)* -- x coordinates.
      * **y** *(array)* -- y coordinates.


.. function:: coords.cart2sphere(x, y, z[, center=[0., 0., 0.]])

    Returns the polar coordinates for a given set of cartesian coordinates.

    :param x: x coordinates.
    :type x: array
    :param y: y coordinates.
    :type y: array
    :param z: z coordinates.
    :type z: array
    :param center: Center point of spherical polar coordinate grid.
    :type center: list

    :returns:
      * **r** *(array)* -- Radial coordinates.
      * **phi** *(array)* -- Phi coordinates.
      * **theta** *(array)* -- Theta coordinates.


.. function:: coords.polar2sphere(r, phi, theta[, center=[0., 0., 0.]])

    Returns the polar coordinates for a given set of cartesian coordinates.

    :param r: Radial coordinates.
    :type r: array
    :param phi: Phi coordinates.
    :type phi: array
    :param theta: Theta coordinates.
    :type theta: array
    :param center: Center point of polar coordinate grid.
    :type center: list

    :returns:
      * **x** *(array)* -- x coordinates.
      * **y** *(array)* -- y coordinates.
      * **z** *(array)* -- z coordinates.


.. function:: coords.ortho2cart(x, y[, r= 1., fill_value=np.nan])

    Orthographic projection to cartesian coordinates.

    :param x: x coordinates.
    :type x: array
    :param y: y coordinates.
    :type y: array
    :param r: Radius of the sphere.
    :type r: float
    :param fill_value: Values outside the sphere are assigned this value.
    :type fill_value: float

    :returns: **z** *(array)* -- Returns the z value of the cartesian coordinates.


Rotations
---------


Utility
-------
