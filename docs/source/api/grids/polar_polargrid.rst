
magpie.grids.polargrid
^^^^^^^^^^^^^^^^^^^^^^^


.. function:: magpie.grids.polargrid(nr, nphi[, rmin=0., rmax=1., phimin=0., phimax=2*np.pi, returns1d=False])

    Constructs a polar coordinate grid.

    :Parameters:
      nr : int
          Number of divisions along the r-axis.
      nphi : int
          Number of divisions along the p-axis.
      rmin : float, optional
          Minimum radial value, default=0.
      rmax : float, optional
          Maximum radial value, default=1.
      phimin : float, optional
          Minimum phi value, default=0.
      phimax : float, optional
          Maximum phi value, default=2pi.
      return1d : bool, optional
          Returns 1d mid-points.

    :Returns:
      r2d, p2d : 2darray
          Radial and phi grid points in 2darray.
      rmid, pmid : array, optional
          The mid-point of the polar grid.
