# MAGPIE: Monte cArlo weiGhted PIxel rEmapping

[![PyPI version](https://badge.fury.io/py/magpie-pkg.svg)](https://badge.fury.io/py/magpie-pkg)
[![Anaconda-Server Badge](https://anaconda.org/knaidoo29/magpie-pkg/badges/version.svg)](https://anaconda.org/knaidoo29/magpie-pkg)
[![Documentation Status](https://readthedocs.org/projects/magpie-doc/badge/?version=latest)](https://magpie-doc.readthedocs.io/en/latest/?badge=latest)
[![CircleCI](https://circleci.com/gh/knaidoo29/magpie/tree/master.svg?style=svg)](https://circleci.com/gh/knaidoo29/magpie/tree/master)
[![codecov](https://codecov.io/gh/knaidoo29/magpie/branch/development/graph/badge.svg?token=P7H8FAJT43)](https://codecov.io/gh/knaidoo29/magpie)
[comment]: # ([![codecov](https://codecov.io/gh/knaidoo29/magpie/branch/master/graph/badge.svg?token=P7H8FAJT43)](https://codecov.io/gh/knaidoo29/magpie))

[![Anaconda-Server Badge](https://anaconda.org/knaidoo29/magpie-pkg/badges/license.svg)](https://anaconda.org/knaidoo29/magpie-pkg)

|               |                                       |
|---------------|---------------------------------------|
| Author        | Krishna Naidoo                        |          
| Version       | 0.3-alpha                             |
| Repository    | https://github.com/knaidoo29/magpie   |
| Documentation | https://magpie-doc.readthedocs.io/    |

> **_WARNING:_** This is the development branch of MAGPIE used to develop and build new functions and classes. Users should clone the main branch for their uses.

## To-Do for **Version 1**

* Grids
  - [x] Uniform 1D, 2D, 3D Grids.
  - [ ] Non-Uniform Grids.
  - [x] Polar grid and Equal Area Grid
  - [ ] Usphere grid and healpix.
  - [ ] Spherical cap equal area grid
  - [ ] Spherial polar coordinate grid + healpix, equal volume grid if possible.
* Coordinates
  - [x] 2D cartesian to polar.
  - [x] 3D cartesian to spherical polar.
  - [x] Healpix angular to healpix x and y.
  - [x] Rotations in 2D and 3D.
  - [ ] 2D to new 2D given new x-axis or y-axis
  - [ ] 3D to new 3D given new x, y, z with only 2 required.
  - [ ] Clear up routines for orthoscopic projections.
  - [ ] Line + thickness in 2D and usphere.
  - [ ] Cartesian to Cylindrical coordinates along arbitrary line segment.
  - [ ] Line + thickness in 3D.
  - [ ] Perspective/Camera view and transform.
  - [ ] 3D slices -> lines, planes, discs.
* Pixels
  - [ ] Computing pixel length, area or volumes.
  - [ ] Fast pixel ID finding based on position in space (consider linear interpolation for non-uniform grid).
* Remapping
  - [ ] Cartesian grid remapping computed exactly.
  - [ ] Generalised 2D and 3D remapping requiring only the end point grids and the methods for computation (i.e. MC or HR) with support for weights and uncertainties.
  - [ ] Storing and computing weights for generic environment.
  - [ ] Dynamic MC randoms dependent on pixel area and dynamic HR again depending on pixel area to prevent aliasing.
  - [ ] Mean and sum functions along an axis or a grid.
  - [ ] Masking and computation of a subset of weights.
* Plotting
  - [ ] Routines for plotting grids in various coordinate systems and for specifying axes and grid lines.
* Testing
  - [ ] Setup tox for different environments (perhaps even platforms) with CircleCI.
* Tutorials
  - [ ] Tutorial scripts which can be downloaded and are showcased on readthedocs.
  - [ ] Jupyter notebooks for seamless integration with binder.

## Introduction

MAGPIE is a python module for remapping bins (in 1D), pixels (in 2D) and cells (in 3D) into different coordinate systems. The package will enable data to be remapped from cartesian to polar coordinates, cartesian to spherical polar coordinates and will enable rotations of these systems. When carrying out coordinate transformations we typically take the center of the pixel or cell and apply the transform without considering the surface area of the pixel (or volume of the cell). In MAGPIE this is taken into account by applying two remapping schemes. The first weights pixels to a new coordinate grid using monte-carlo integration. The second uses a higher-resolution mesh (denser than the new coordinate grid by some integer factor along each dimension) which is rebinned to the target coordinate grid. In both cases we sample the surface area or volume of the new coordinate pixels to accurately remap the data. The monte-carlo method is more accurate but scales poorly to 3D. For 2D this scheme will work very well even for moderately large datasets. The higher-resolution mesh method, while less accurate, is very fast and should be used for large data sets and all 3D transformations. In 1D these are computed exactly without requiring the approximate schemes above.

> **_NOTE:_**  MPI functionality is currently unavailable but the plan will be to implement this using mpi4py and an additional library MPIutils which will handle all of the MPI enabled functions.

## Dependencies

MAGPIE is being developed in Python 3.9 but should work on all versions >=3.4. MAGPIE is written mostly in python but with some heavy computation carried out in Fortran. Compiling the Fortran source code will require the availability of a fortran compiler such as gfortran or ifort.

The following Python modules are required:

* [numpy](http://www.numpy.org/)
* [scipy](https://scipy.org/)
* [healpy](https://healpy.readthedocs.io/)

For testing you will require [nose](https://nose.readthedocs.io/en/latest/) or [pytest](http://pytest.org/en/latest/).


## Installation

MAGPIE can be installed in a variety of ways -- using `conda`, `pip` or by directly cloning the repository. If you are having trouble installing or running MAGPIE we recommend using the conda install as this will setup the environment.

1. Using `conda`:

  ```
      conda install -c knaidoo29 magpie-pkg
  ```

2. Using `pip`:

  ```
      pip install magpie-pkg
  ```

3. By cloning the github repository:

  ```
      git clone https://github.com/knaidoo29/magpie.git
      cd magpie
      python setup.py build
      python setup.py install
  ```

Once this is done you should be able to call `magpie` from python:

```
    import magpie
```

## Support

If you have any issues with the code or want to suggest ways to improve it please open a new issue ([here](https://github.com/knaidoo29/magpie/issues)) or (if you don't have a github account) email _krishna.naidoo.11@ucl.ac.uk_.

## Version History

* **Version 0.3**:
    * Rewrite and removal of **Version 0.1** functions and classes.
    * Coordinate transformation tools: 2D <-> polar, 3D <-> spherical polar, healpix angular <-> healpix x and y, usphere <-> lon/lat, 2D rotations, 3D rotations via Euler angles and Rodrigues rotation formula.
    * Grid definitions: cartesian 1D, 2D & 3D, polar grid and polar equal area grid.
    * Pixel functions: basic shapes -> square, arc, disc and box, healpix pixel boundaries and healpix pixel index conversion functions.
    * Randoms functions: uniform randoms in cartesian 1D, 2D & 3D, polar, unit sphere, spherical polar, healpix pixels. Randoms from user defined PDF/CDF and random and probabilistic subsampling.
    * Limited remapping functions for uniform grids without rotations computed exactly for 1D, 2D & 3D.

* **Version 0.2**:
    * Restructured layout and the incorporation of documentation and unit testing for eventual first release.
    * Randoms in a variety of coordinate systems: cartesian, polar, spherical and from an input PDF/CDF and subsampling and stochastic weights.
    * Cartesian coordinate remapping in 1D, 2D and 3D.
    * Legacy **version 0.1** functions and classes remain.

* **Version 0.1**:
    * Coordinate transformations between cartesian, polar and spherical polar coordinates.
    * Rebinning in 1D (computed exactly), in 2D and 3D via monte-carlo weighted remapping and a dense mesh.
    * Randoms in cartesian, polar and spherical polar coordinates.
    * Rotation transformations.
    * Polar coordinate utilities and integration for polar grid to radial profiles.
    * Plotting routine for orthographic projection of unit sphere data.
