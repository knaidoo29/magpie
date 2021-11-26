
magpie.grids.polarEA_grid
^^^^^^^^^^^^^^^^^^^^^^^^^


.. function:: magpie.grids.polarEA_grid(nr[, rmax=1., base_nphi=4])

    Constructs an equal area polar grid.

    :Parameters:
      nr : int
          Number of divisions along the r-axis.
      rmax : float, optional
          Maximum radial value, default=1.
      base_nphi : int, optional
          Number of pixels around r=0, default=4.

    :Returns:
      r, p : array
          Radial and phi mid points for each pixel in the equal area polar grid.
