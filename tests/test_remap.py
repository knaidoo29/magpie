import numpy as np
import magpie


def test_grid2grid1D():
    # test the grid2grid1D function for different options.
    ngridin = 100
    boxsize = 100.
    ngridout = 50
    f = np.random.random_sample(ngridin)
    fout = magpie.remap.grid2grid1D(f, boxsize, ngridout)
    fout = magpie.remap.grid2grid1D(f, boxsize, ngridout, origin=50.)
    fout = magpie.remap.grid2grid1D(f, boxsize, ngridout, originout=50.)
    fout = magpie.remap.grid2grid1D(f, boxsize, ngridout, boxsizeout=50.)


def test_grid2grid2D():
    # test the grid2grid2D function for different options.
    ngridin = 100
    boxsize = 100.
    ngridout = 50
    f = np.random.random_sample((ngridin, ngridin))
    fout = magpie.remap.grid2grid2D(f, boxsize, ngridout)
    fout = magpie.remap.grid2grid2D(f, [boxsize, boxsize/2], ngridout)
    fout = magpie.remap.grid2grid2D(f, boxsize, [ngridout, int(ngridout/2)])
    fout = magpie.remap.grid2grid2D(f, boxsize, ngridout, origin=50.)
    fout = magpie.remap.grid2grid2D(f, boxsize, ngridout, origin=[50., -50])
    fout = magpie.remap.grid2grid2D(f, boxsize, ngridout, originout=50.)
    fout = magpie.remap.grid2grid2D(f, boxsize, ngridout, originout=[50., -50.])
    fout = magpie.remap.grid2grid2D(f, boxsize, ngridout, boxsizeout=50.)
    fout = magpie.remap.grid2grid2D(f, boxsize, ngridout, boxsizeout=[50., 40.])
    f = np.random.random_sample((ngridin, int(ngridin/2)))
    fout = magpie.remap.grid2grid2D(f, boxsize, ngridout)

def test_grid2grid3D():
    # test the grid2grid2D function for different options.
    ngridin = 100
    boxsize = 100.
    ngridout = 50
    f = np.random.random_sample((ngridin, ngridin, ngridin))
    fout = magpie.remap.grid2grid3D(f, boxsize, ngridout)
    fout = magpie.remap.grid2grid3D(f, [boxsize, boxsize/2, boxsize*2], ngridout)
    fout = magpie.remap.grid2grid3D(f, boxsize, [ngridout, int(ngridout/2), int(ngridout*3)])
    fout = magpie.remap.grid2grid3D(f, boxsize, ngridout, origin=50.)
    fout = magpie.remap.grid2grid3D(f, boxsize, ngridout, origin=[50., -50., -20.])
    fout = magpie.remap.grid2grid3D(f, boxsize, ngridout, originout=50.)
    fout = magpie.remap.grid2grid3D(f, boxsize, ngridout, originout=[50., -50., 40.])
    fout = magpie.remap.grid2grid3D(f, boxsize, ngridout, boxsizeout=50.)
    fout = magpie.remap.grid2grid3D(f, boxsize, ngridout, boxsizeout=[50., 40., 60.])
    f = np.random.random_sample((ngridin, int(ngridin/2), int(ngridin*4)))
    fout = magpie.remap.grid2grid3D(f, boxsize, ngridout)
