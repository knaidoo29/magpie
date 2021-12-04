
magpie.pixels.pos2pix_cart1d
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. function:: magpie.pixels.pos2pix_cart1d(x, length, ngrid[, xmin=0.])

    X-coordinate to 1D pixel.

    :Parameters:
      x : float or array
          X-coordinate.
      length : float
          Length of the 1D grid.
      ngrid : int
          The grid dimension.
      xmin : float, optional
          Minimum value along the grid.

    :Returns:
      pixID : int or array
          The index of the pixel the points are located in.
