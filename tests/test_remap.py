import numpy as np
import magpie


def test_grid2grid1d():
    # test the grid2grid1d function for different options.
    ngridin = 100
    boxsize = 100.
    ngridout = 50
    f = np.random.random_sample(ngridin)
    fout = magpie.remap.grid2grid1d(f, boxsize, ngridout)
    fout = magpie.remap.grid2grid1d(f, boxsize, ngridout, origin=50.)
    fout = magpie.remap.grid2grid1d(f, boxsize, ngridout, originout=50.)
    fout = magpie.remap.grid2grid1d(f, boxsize, ngridout, boxsizeout=50.)


def test_grid2grid2d():
    # test the grid2grid2d function for different options.
    ngridin = 100
    boxsize = 100.
    ngridout = 50
    f = np.random.random_sample((ngridin, ngridin))
    fout = magpie.remap.grid2grid2d(f, boxsize, ngridout)
    f = np.random.random_sample((ngridin, ngridin))
    fout = magpie.remap.grid2grid2d(f, [boxsize, boxsize/2], ngridout)
    f = np.random.random_sample((ngridin, ngridin))
    fout = magpie.remap.grid2grid2d(f, boxsize, [ngridout, int(ngridout/2)])
    f = np.random.random_sample((ngridin, ngridin))
    fout = magpie.remap.grid2grid2d(f, boxsize, ngridout, origin=50.)
    f = np.random.random_sample((ngridin, ngridin))
    fout = magpie.remap.grid2grid2d(f, boxsize, ngridout, origin=[50., -50])
    f = np.random.random_sample((ngridin, ngridin))
    fout = magpie.remap.grid2grid2d(f, boxsize, ngridout, originout=50.)
    f = np.random.random_sample((ngridin, ngridin))
    fout = magpie.remap.grid2grid2d(f, boxsize, ngridout, originout=[50., -50.])
    f = np.random.random_sample((ngridin, ngridin))
    fout = magpie.remap.grid2grid2d(f, boxsize, ngridout, boxsizeout=50.)
    f = np.random.random_sample((ngridin, ngridin))
    fout = magpie.remap.grid2grid2d(f, boxsize, ngridout, boxsizeout=[50., 40.])
    f = np.random.random_sample((ngridin, int(ngridin/2)))
    fout = magpie.remap.grid2grid2d(f, boxsize, ngridout)

def test_grid2grid3d():
    # test the grid2grid2d function for different options.
    ngridin = 100
    boxsize = 100.
    ngridout = 50
    f = np.random.random_sample((ngridin, ngridin, ngridin))
    fout = magpie.remap.grid2grid3d(f, boxsize, ngridout)
    f = np.random.random_sample((ngridin, ngridin, ngridin))
    fout = magpie.remap.grid2grid3d(f, [boxsize, boxsize/2, boxsize*2], ngridout)
    f = np.random.random_sample((ngridin, ngridin, ngridin))
    fout = magpie.remap.grid2grid3d(f, boxsize, [ngridout, int(ngridout/2), int(ngridout*3)])
    f = np.random.random_sample((ngridin, ngridin, ngridin))
    fout = magpie.remap.grid2grid3d(f, boxsize, ngridout, origin=50.)
    f = np.random.random_sample((ngridin, ngridin, ngridin))
    fout = magpie.remap.grid2grid3d(f, boxsize, ngridout, origin=[50., -50., -20.])
    f = np.random.random_sample((ngridin, ngridin, ngridin))
    fout = magpie.remap.grid2grid3d(f, boxsize, ngridout, originout=50.)
    f = np.random.random_sample((ngridin, ngridin, ngridin))
    fout = magpie.remap.grid2grid3d(f, boxsize, ngridout, originout=[50., -50., 40.])
    f = np.random.random_sample((ngridin, ngridin, ngridin))
    fout = magpie.remap.grid2grid3d(f, boxsize, ngridout, boxsizeout=50.)
    f = np.random.random_sample((ngridin, ngridin, ngridin))
    fout = magpie.remap.grid2grid3d(f, boxsize, ngridout, boxsizeout=[50., 40., 60.])
    f = np.random.random_sample((ngridin, int(ngridin/2), int(ngridin*4)))
    fout = magpie.remap.grid2grid3d(f, boxsize, ngridout)
