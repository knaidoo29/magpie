import numpy as np
import matplotlib.pylab as plt
from matplotlib.collections import PatchCollection

from .. import grids
from .. import pixels


def plot_polarEA(pix, nr=None, rmax=1., base_nphi=3, pixID=None, proj='cart',
                 center=[0., 0.], steps=12, ax=None, vmin=None, vmax=None,
                 cmap=plt.cm.viridis):
    """Plots pixels from a polar equal area grid.

    Parameters
    ----------
    pix : array
        Pixel values.
    nr : int, optional
        Enter the number of radial bins, if None this will be calculated from
        the size of pix and base_nphi.
    rmax : float, optional
        Maximum radius, default=1.
    base_nphi: int, optional
        Number of pixels in the first ring, default=3.
    pixID : int, optional
        Enter the pixel indices of pix if pix is a subset of the pixel grid.
        Useful if you wish to plot only a subset of the pixel grid.
    proj : str, optional
        Output coordinate projection. Either 'cart' for cartesian or 'polar'
        for polar projection.
    center : list, optional
        Center point of the polar grid, only relevant for cartesian
        projection, default at the origin.
    steps : int, optional
        Number of steps in the polygon, default=12.
    ax : obj, optional
        Matplotlib axis, if None this is plotted onto the last figure.
    vmin, vmax : float, optional
        Ranges for pixel color.
    cmap : obj, optional
        Enter matplotlib colormap object, default=plt.cm.viridis.
    """
    if pixID is None:
        if nr is None:
            nr = int(np.sqrt(len(pix)/base_nphi))
        npix = grids.polarEA_npix(nr, base_nphi)
        pixID = np.arange(npix)
    else:
        assert nr is not None, "nr must be defined if pixID is given."
    if vmin is None:
        vmin = np.min(pix[np.isfinite(pix)])
    if vmax is None:
        vmax = np.max(pix[np.isfinite(pix)])
    cval = pix - vmin
    if vmin != vmax:
        cval /= vmax - vmin
    colors = cmap(cval)
    patches = [pixels.get_polarEA_shape(pixID[i], nr, rmax=rmax,
                                        base_nphi=base_nphi, proj=proj,
                                        center=[0., 0.], steps=12,
                                        returnpoly=True)
               for i in range(0, len(pixID))]
    patch_coll = PatchCollection(patches, facecolors=colors, edgecolor="none")
    if ax is None:
        plt.gcf().gca().add_collection(patch_coll)
    else:
        ax.add_collection(patch_coll)
