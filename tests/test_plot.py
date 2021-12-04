import numpy as np
import matplotlib.pylab as plt
import magpie


def test_plot_polarEA():
    nr, base_nphi = 10, 3
    npix = magpie.grids.polarEA_npix(nr, base_nphi)
    pixID = np.arange(npix)
    pix = np.ones(npix)
    plt.figure()
    magpie.plot.plot_polarEA(pix)
    plt.close()
    pix = np.random.random_sample(npix)
    plt.figure()
    magpie.plot.plot_polarEA(pix, nr=nr, pixID=pixID)
    plt.close()
    fig, ax = plt.subplots(1, 1)
    magpie.plot.plot_polarEA(pix, ax=ax)
    plt.close()
