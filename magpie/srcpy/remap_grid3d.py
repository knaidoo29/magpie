import numpy as np
from numba import njit

from . import pixel_1dto3d
from . import remap_utils


@njit
def remap_3d_grid2grid(x1min, x1max, x1grid, y1min, y1max, y1grid, z1min, z1max, z1grid,
                       x2min, x2max, x2grid, y2min, y2max, y2grid, z2min, z2max, z2grid,
                       xyz1grid, xyz2grid, xpixlen, ypixlen, zpixlen, xyzpixlen, f1):
    """
    Remaps field 1 onto field 2 using exact weights in 3D.

    Parameters
    ----------
    x1min, x1max : float
        Minimum and maximum x in grid 1.
    x1grid : int
        Number of grid points in grid 1 along x.
    y1min, y1max : float
        Minimum and maximum y in grid 1.
    y1grid : int
        Number of grid points in grid 1 along y.
    z1min, z1max : float
        Minimum and maximum z in grid 1.
    z1grid : int
        Number of grid points in grid 1 along z.
    x2min, x2max : float
        Minimum and maximum x in grid 2.
    x2grid : int
        Number of grid points in grid 2 along x.
    y2min, y2max : float
        Minimum and maximum y in grid 2.
    y2grid : int
        Number of grid points in grid 2 along y.
    z2min, z2max : float
        Minimum and maximum z in grid 2.
    z2grid : int
        Number of grid points in grid 2 along z.
    xyz1grid : int
        Flattened number of grid points in grid 1.
    xyz2grid : int
        Flattened number of grid points in grid 2.
    xpixlen, ypixlen, zpixlen : int
        Length of pixel mapping indices and weights along x, y, and z.
    xyzpixlen : int
        Length of pixel mapping indices flattened for xyz.
    f1 : array
        Field values on grid 1.

    Returns
    -------
    f2 : array
        Remapped field on grid 2.
    """
    # Initialize the output field f2
    f2 = np.zeros(xyz2grid, dtype=np.float64)

    # Loop over each pixel in grid 2 (x, y, z)
    for i in range(x2grid):
        xwhich2pix = i  # Pixel in grid 2 along x

        # Get the pixel IDs and weights for the current pixel along x
        xpix_id, xweights = remap_utils.remap_1d_grid2grid_pixel(x1min, x1max, x1grid, x2min, x2max, x2grid, xwhich2pix, xpixlen)

        for j in range(y2grid):
            ywhich2pix = j  # Pixel in grid 2 along y

            # Get the pixel IDs and weights for the current pixel along y
            ypix_id, yweights = remap_utils.remap_1d_grid2grid_pixel(y1min, y1max, y1grid, y2min, y2max, y2grid, ywhich2pix, ypixlen)

            for k in range(z2grid):
                zwhich2pix = k  # Pixel in grid 2 along z

                # Get the pixel IDs and weights for the current pixel along z
                zpix_id, zweights = remap_utils.remap_1d_grid2grid_pixel(z1min, z1max, z1grid, z2min, z2max, z2grid, zwhich2pix, zpixlen)

                # Flatten the 3D pixel IDs into a 1D array for the remapping process
                pix_id = pixel_1dto3d.pix_id_1dto3d_grid(xpix_id, ypix_id, zpix_id, y1grid, z1grid)

                ii = zwhich2pix + z2grid * (ywhich2pix + y2grid * xwhich2pix)  # Flattened index for grid 2
                f2[ii] = 0.0  # Initialize the field value

                jj = 0  # Pixel counter

                # Loop over the pixels along x, y, and z
                for i1 in range(xpixlen):
                    for j1 in range(ypixlen):
                        for k1 in range(zpixlen):
                            if pix_id[jj] != -1:
                                # Update the field value using the pixel weights and field values from grid 1
                                f2[ii] += xweights[i1] * yweights[j1] * zweights[k1] * f1[pix_id[jj]]
                            jj += 1

    return f2
