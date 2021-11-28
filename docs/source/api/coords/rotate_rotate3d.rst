
magpie.coords.rotate3d
^^^^^^^^^^^^^^^^^^^^^^

.. function:: magpie.coords.rotate3d(x, y, z, angles[, axes='zyz', center=[0., 0., 0.]]):

    Rotates points in 3D cartesian coordinates by Euler angle around
    specified axes.

    :Parameters:
      x, y, z : float or array
          Cartesian coordinates.
      angles : array
          Euler angles.
      axes : str, optional
          Euler angle axes, default z-y-z rotations.
      center : list[float], optional
          Center of rotation, default=[0., 0., 0.].

    :Returns:
      xrot, yrot, zrot : float or array
