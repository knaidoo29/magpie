import numpy as np
import magpie


# check cartesian

def test_get_xedges():
    xedges = magpie.grids.get_xedges(1., 2)
    xedges = np.round(xedges, decimals=2)
    assert len(xedges) == 3, "Length of xedges is incorrect."
    assert xedges[-1] - xedges[0] == 1., "xedges range is incorrect."
    xedges = magpie.grids.get_xedges(1., 2, xmin=-1.)
    xedges = np.round(xedges, decimals=2)
    assert xedges[0]==-1. and xedges[1]==-0.5 and xedges[-1]==0., "xedges with xmin are not as expected."
    assert xedges[-1] - xedges[0] == 1., "xedges range is incorrect."

def test_xedges2mid():
    xedges = magpie.grids.get_xedges(1., 10)
    xmid = magpie.grids.xedges2mid(xedges)
    xmid = np.round(xmid, decimals=2)
    assert len(xedges) == len(xmid) + 1, "Length of xmid is incorrect."
    assert xmid[0] == 0.05 and xmid[1] == 0.15 and xmid[5] == 0.55, "xmid is not as expected."

def test_xmid2edges():
    xedges = magpie.grids.get_xedges(1., 10)
    xmid = magpie.grids.xedges2mid(xedges)
    xedges2 = np.round(magpie.grids.xmid2edges(xmid), decimals=2)
    assert np.sum(xedges-xedges2), "Conversion from xmid to xedges is not consistent with input xedges."

def test_grid1d():
    xmid = magpie.grids.grid1d(10., 10)
    assert np.round(xmid[0], decimals=4) == 0.5 and np.round(xmid[7], decimals=4) == 7.5, "grid1d unexpected results."
    xmid = magpie.grids.grid1d(10., 10, xmin=10)
    assert np.round(xmid[0], decimals=4) == 10.5 and np.round(xmid[7], decimals=4) == 17.5, "grid1d unexpected results."
    xmid, xedges = magpie.grids.grid1d(10., 10, return_edges=True)
    assert len(xmid)+1 == len(xedges), "Length of xmid and xedges is not as expected."
    assert np.round(xedges[0], decimals=4) == 0. and np.round(xedges[7], decimals=4) == 7., "grid1d unexpected results."
    assert np.round(xmid[0], decimals=4) == 0.5 and np.round(xmid[7], decimals=4) == 7.5, "grid1d unexpected results."

def test_grid2d():
    x2d, y2d = magpie.grids.grid2d(10, 10)
    assert np.shape(x2d) == (10, 10), "shape is not as expected."
    assert np.shape(y2d) == (10, 10), "shape is not as expected."
    x2d, y2d, xmid, ymid = magpie.grids.grid2d(10, 10, return1d=True)
    assert np.round(xmid[0], decimals=4) == 0.5 and np.round(xmid[7], decimals=4) == 7.5, "grid2d unexpected results."
    assert np.round(np.sum(np.unique(x2d.flatten())-xmid), decimals=4) == 0., "xmid is inconsistent with x2d."
    assert np.round(ymid[0], decimals=4) == 0.5 and np.round(ymid[7], decimals=4) == 7.5, "grid2d unexpected results."
    assert np.round(np.sum(np.unique(y2d.flatten())-ymid), decimals=4) == 0., "ymid is inconsistent with y2d."
    x2d, y2d, xmid, ymid = magpie.grids.grid2d(10, 10, mins=[10., 20.], return1d=True)
    assert np.round(xmid[0], decimals=4) == 10.5 and np.round(xmid[7], decimals=4) == 17.5, "grid2d unexpected results."
    assert np.round(np.sum(np.unique(x2d.flatten())-xmid), decimals=4) == 0., "xmid is inconsistent with x2d."
    assert np.round(ymid[0], decimals=4) == 20.5 and np.round(ymid[7], decimals=4) == 27.5, "grid2d unexpected results."
    assert np.round(np.sum(np.unique(y2d.flatten())-ymid), decimals=4) == 0., "ymid is inconsistent with y2d."
    x2d, y2d = magpie.grids.grid2d(10, [10, 20])
    assert np.shape(x2d) == (10, 20), "shape is not as expected."
    assert np.shape(y2d) == (10, 20), "shape is not as expected."
    x2d, y2d, xmid, ymid = magpie.grids.grid2d([10, 20], [10, 20], return1d=True)
    assert np.round(xmid[0], decimals=4) == 0.5 and np.round(xmid[7], decimals=4) == 7.5, "grid2d unexpected results."
    assert np.round(np.sum(np.unique(x2d.flatten())-xmid), decimals=4) == 0., "xmid is inconsistent with x2d."
    assert np.round(ymid[0], decimals=4) == 0.5 and np.round(ymid[7], decimals=4) == 7.5, "grid2d unexpected results."
    assert np.round(np.sum(np.unique(y2d.flatten())-ymid), decimals=4) == 0., "ymid is inconsistent with y2d."
    x2d, y2d, xmid, ymid = magpie.grids.grid2d([10, 20], [10, 20], mins=[10., 20.], return1d=True)
    assert np.round(xmid[0], decimals=4) == 10.5 and np.round(xmid[7], decimals=4) == 17.5, "grid2d unexpected results."
    assert np.round(np.sum(np.unique(x2d.flatten())-xmid), decimals=4) == 0., "xmid is inconsistent with x2d."
    assert np.round(ymid[0], decimals=4) == 20.5 and np.round(ymid[7], decimals=4) == 27.5, "grid2d unexpected results."
    assert np.round(np.sum(np.unique(y2d.flatten())-ymid), decimals=4) == 0., "ymid is inconsistent with y2d."


def test_grid3d():
    x3d, y3d, z3d = magpie.grids.grid3d(10, 10)
    assert np.shape(x3d) == (10, 10, 10), "shape is not as expected."
    assert np.shape(y3d) == (10, 10, 10), "shape is not as expected."
    assert np.shape(z3d) == (10, 10, 10), "shape is not as expected."
    x3d, y3d, z3d, xmid, ymid, zmid = magpie.grids.grid3d(10, 10, return1d=True)
    assert np.round(xmid[0], decimals=4) == 0.5 and np.round(xmid[7], decimals=4) == 7.5, "grid3d unexpected results."
    assert np.round(np.sum(np.unique(x3d.flatten())-xmid), decimals=4) == 0., "xmid is inconsistent with x3d."
    assert np.round(ymid[0], decimals=4) == 0.5 and np.round(ymid[7], decimals=4) == 7.5, "grid3d unexpected results."
    assert np.round(np.sum(np.unique(y3d.flatten())-ymid), decimals=4) == 0., "ymid is inconsistent with y3d."
    assert np.round(zmid[0], decimals=4) == 0.5 and np.round(zmid[7], decimals=4) == 7.5, "grid3d unexpected results."
    assert np.round(np.sum(np.unique(z3d.flatten())-zmid), decimals=4) == 0., "zmid is inconsistent with z3d."
    x3d, y3d, z3d, xmid, ymid, zmid = magpie.grids.grid3d(10, 10, mins=[10., 20., 30.], return1d=True)
    assert np.round(xmid[0], decimals=4) == 10.5 and np.round(xmid[7], decimals=4) == 17.5, "grid3d unexpected results."
    assert np.round(np.sum(np.unique(x3d.flatten())-xmid), decimals=4) == 0., "xmid is inconsistent with x3d."
    assert np.round(ymid[0], decimals=4) == 20.5 and np.round(ymid[7], decimals=4) == 27.5, "grid3d unexpected results."
    assert np.round(np.sum(np.unique(y3d.flatten())-ymid), decimals=4) == 0., "ymid is inconsistent with y3d."
    assert np.round(zmid[0], decimals=4) == 30.5 and np.round(zmid[7], decimals=4) == 37.5, "grid3d unexpected results."
    assert np.round(np.sum(np.unique(z3d.flatten())-zmid), decimals=4) == 0., "zmid is inconsistent with z3d."
    x3d, y3d, z3d = magpie.grids.grid3d(10, [10, 20, 30])
    assert np.shape(x3d) == (10, 20, 30), "shape is not as expected."
    assert np.shape(y3d) == (10, 20, 30), "shape is not as expected."
    assert np.shape(z3d) == (10, 20, 30), "shape is not as expected."
    x3d, y3d, z3d, xmid, ymid, zmid = magpie.grids.grid3d([10, 20, 30], [10, 20, 30], return1d=True)
    assert np.round(xmid[0], decimals=4) == 0.5 and np.round(xmid[7], decimals=4) == 7.5, "grid3d unexpected results."
    assert np.round(np.sum(np.unique(x3d.flatten())-xmid), decimals=4) == 0., "xmid is inconsistent with x3d."
    assert np.round(ymid[0], decimals=4) == 0.5 and np.round(ymid[7], decimals=4) == 7.5, "grid3d unexpected results."
    assert np.round(np.sum(np.unique(y3d.flatten())-ymid), decimals=4) == 0., "ymid is inconsistent with y3d."
    assert np.round(zmid[0], decimals=4) == 0.5 and np.round(zmid[7], decimals=4) == 7.5, "grid3d unexpected results."
    assert np.round(np.sum(np.unique(z3d.flatten())-zmid), decimals=4) == 0., "zmid is inconsistent with z3d."
    x3d, y3d, z3d, xmid, ymid, zmid = magpie.grids.grid3d([10, 20, 30], [10, 20, 30], mins=[10., 20., 30], return1d=True)
    assert np.round(xmid[0], decimals=4) == 10.5 and np.round(xmid[7], decimals=4) == 17.5, "grid3d unexpected results."
    assert np.round(np.sum(np.unique(x3d.flatten())-xmid), decimals=4) == 0., "xmid is inconsistent with x3d."
    assert np.round(ymid[0], decimals=4) == 20.5 and np.round(ymid[7], decimals=4) == 27.5, "grid3d unexpected results."
    assert np.round(np.sum(np.unique(y3d.flatten())-ymid), decimals=4) == 0., "ymid is inconsistent with y3d."
    assert np.round(zmid[0], decimals=4) == 30.5 and np.round(zmid[7], decimals=4) == 37.5, "grid3d unexpected results."
    assert np.round(np.sum(np.unique(z3d.flatten())-zmid), decimals=4) == 0., "zmid is inconsistent with z3d."


# check polar

def test_polargrid():
    r2d, p2d = magpie.grids.polargrid(10, 20)
    assert np.shape(r2d) == (10, 20), "shape is not as expected."
    assert np.shape(p2d) == (10, 20), "shape is not as expected."
    r2d, p2d, rmid, pmid = magpie.grids.polargrid(10, 20, return1d=True)
    assert np.round(rmid[0], decimals=4) == 0.05 and np.round(rmid[7], decimals=4) == 0.75, "polargrid unexpected results."
    assert np.round(np.sum(np.unique(r2d.flatten())-rmid), decimals=4) == 0., "rmid is inconsistent with r2d."
    assert np.round(pmid[0], decimals=4) == np.round(np.pi/20, decimals=4) and np.round(pmid[7], decimals=4) == np.round(15*np.pi/20, decimals=4), "polargrid unexpected results."
    assert np.round(np.sum(np.unique(p2d.flatten())-pmid), decimals=4) == 0., "pmid is inconsistent with p2d."
    r2d, p2d, rmid, pmid = magpie.grids.polargrid(10, 10, rmin=10., rmax=20., phimin=np.pi/2., phimax=np.pi, return1d=True)
    assert np.round(rmid[0], decimals=4) == 10.5 and np.round(rmid[7], decimals=4) == 17.5, "polargrid unexpected results."
    assert np.round(np.sum(np.unique(r2d.flatten())-rmid), decimals=4) == 0., "rmid is inconsistent with r2d."
    assert np.round(pmid[0], decimals=4) == np.round((np.pi/2.)/20 + np.pi/2., decimals=4) \
        and np.round(pmid[7], decimals=4) == np.round(15*(np.pi/2.)/20 + np.pi/2., decimals=4), "polargrid unexpected results."
    assert np.round(np.sum(np.unique(p2d.flatten())-pmid), decimals=4) == 0., "pmid is inconsistent with p2d."


def test_polargrid():
    r2d, p2d = magpie.grids.polargrid(10, 20)
    assert np.shape(r2d) == (10, 20), "shape is not as expected."
    assert np.shape(p2d) == (10, 20), "shape is not as expected."
    r2d, p2d, rmid, pmid = magpie.grids.polargrid(10, 20, return1d=True)
    assert np.round(rmid[0], decimals=4) == 0.05 and np.round(rmid[7], decimals=4) == 0.75, "polargrid unexpected results."
    assert np.round(np.sum(np.unique(r2d.flatten())-rmid), decimals=4) == 0., "rmid is inconsistent with r2d."
    assert np.round(pmid[0], decimals=4) == np.round(np.pi/20, decimals=4) and np.round(pmid[7], decimals=4) == np.round(15*np.pi/20, decimals=4), "polargrid unexpected results."
    assert np.round(np.sum(np.unique(p2d.flatten())-pmid), decimals=4) == 0., "pmid is inconsistent with p2d."
    r2d, p2d, rmid, pmid = magpie.grids.polargrid(10, 10, rmin=10., rmax=20., phimin=np.pi/2., phimax=np.pi, return1d=True)
    assert np.round(rmid[0], decimals=4) == 10.5 and np.round(rmid[7], decimals=4) == 17.5, "polargrid unexpected results."
    assert np.round(np.sum(np.unique(r2d.flatten())-rmid), decimals=4) == 0., "rmid is inconsistent with r2d."
    assert np.round(pmid[0], decimals=4) == np.round((np.pi/2.)/20 + np.pi/2., decimals=4) \
        and np.round(pmid[7], decimals=4) == np.round(15*(np.pi/2.)/20 + np.pi/2., decimals=4), "polargrid unexpected results."
    assert np.round(np.sum(np.unique(p2d.flatten())-pmid), decimals=4) == 0., "pmid is inconsistent with p2d."

def test_polarEA():
    r, p = magpie.grids.polarEA_grid(10)
    npix = magpie.grids.polarEA_npix(10)
    assert len(r) == len(p), "PolarEA grid size for r and p are not the same."
    assert len(r) == npix, "Length of polarEA grid does not match expectations."
    r, p = magpie.grids.polarEA_grid(6, base_nphi=3)
    npix = magpie.grids.polarEA_npix(6, base_nphi=3)
    assert len(r) == len(p), "PolarEA grid size for r and p are not the same."
    assert len(r) == npix, "Length of polarEA grid does not match expectations."
    r, p = magpie.grids.polarEA_grid(10, base_nphi=3)
    npix = magpie.grids.polarEA_npix(10, base_nphi=3)
    assert len(r) == len(p), "PolarEA grid size for r and p are not the same."
    assert len(r) == npix, "Length of polarEA grid does not match expectations."
    assert r[3*4**2] == 0.45, "r values are incorrect."
    assert r[3*7**2] == 0.75, "r values are incorrect."
    assert np.round(p[3*4**2], decimals=4) == np.round(np.pi/(3*(2*4+1)), decimals=4), "p values are incorrect."
    assert np.round(p[3*7**2 + 7], decimals=4) == np.round(15*np.pi/(3*(2*7+1)), decimals=4), "p values are incorrect."
    area = magpie.grids.polarEA_area(10, rmax=10., base_nphi=4)
    assert(np.round(area, decimals=4) == np.round(np.pi/4., decimals=4)), "area calculation is incorrect."
