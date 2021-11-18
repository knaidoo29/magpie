# MAGPIE: Monte cArlo weiGhted PIxel rEmapping

[![CircleCI](https://circleci.com/gh/knaidoo29/magpie/tree/master.svg?style=svg)](https://circleci.com/gh/knaidoo29/magpie/tree/master)
[![codecov](https://codecov.io/gh/knaidoo29/magpie/branch/master/graph/badge.svg?token=P7H8FAJT43)](https://codecov.io/gh/knaidoo29/magpie)
[![Documentation Status](https://readthedocs.org/projects/magpie-doc/badge/?version=latest)](https://magpie-doc.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/magpie-pkg.svg)](https://badge.fury.io/py/magpie-pkg)
[![Anaconda-Server Badge](https://anaconda.org/knaidoo29/magpie-pkg/badges/installer/conda.svg)](https://conda.anaconda.org/knaidoo29)
[![Anaconda-Server Badge](https://anaconda.org/knaidoo29/magpie-pkg/badges/license.svg)](https://anaconda.org/knaidoo29/magpie-pkg)

|               |                                       |
|---------------|---------------------------------------|
| Author        | Krishna Naidoo                        |          
| Version       | 0.2.1                                 |
| Repository    | https://github.com/knaidoo29/magpie   |
| Documentation | https://magpie-doc.readthedocs.io/    |


## Introduction

MAGPIE is a python module for remapping bins (in 1D), pixels (in 2D) and cells
(in 3D) into different coordinate systems. The package will enable data to be
remapped from cartesian to polar coordinates, cartesian to spherical polar coordinates
and will enable rotations of these systems. When carrying out coordinate transformations
we typically take the center of the pixel or cell and apply the transform without
considering the surface area of the pixel (or volume of the cell). In MAGPIE this is
taken into account by applying two remapping schemes. The first weights pixels to a new
coordinate grid using monte-carlo integration. The second uses a dense grid (denser than
the new coordinate grid) which is rebinned to the target coordinate grid. In both cases
we sample the surface area or volume of the new coordinate pixels to accurately remap the
data. The monte-carlo method is more accurate but scales poorly to 3D. For 2D this scheme
will work very well even for moderately large datasets. The dense grid method, while less
accurate, is very fast and should be used for large data sets and all 3D transformations.
In 1D these are computed exactly without requiring the approximate schemes above.

## Dependencies

MAGPIE is being developed in Python 3.8 but should work on all versions >3.4. MAGPIE
is written mostly in python but with some heavy computation carried out in Fortran.
Compiling the Fortran source code will require the availability of a fortran compiler
usually gfortran (which comes with gcc).

The following Python modules are required.

* [numpy](http://www.numpy.org/)
* [scipy](https://scipy.org/)
* [healpy](https://healpy.readthedocs.io/)

For testing you will require [nose](https://nose.readthedocs.io/en/latest/) or [pytest](http://pytest.org/en/latest/).


## Installation

Magpie can be installed in a variety of ways:

1. Using `pip`:

  ```
      pip install magpie-pkg
  ```

2. Using `conda`:

  ```
      conda install -c knaidoo29 magpie-pkg
  ```

3. By cloning the github repository::

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

If you have any issues with the code or want to suggest ways to improve it please
open a new issue ([here](https://github.com/knaidoo29/magpie/issues)) or (if you don't have a github account) email _krishna.naidoo.11@ucl.ac.uk_.

## Version History

* **Version 0.2**:
    * Restructured layout and the incorporation of documentation and unit testing for eventual first release.
    * Randoms in a variety of coordinate systems: cartesian, polar, spherical and from an input PDF/CDF and subsampling and stochastic weights.
    * Cartesian coordinate remapping in 1D, 2D and 3D.

* **Version 0.1**:
    * Coordinate transformations between cartesian, polar and spherical polar coordinates.
    * Rebinning in 1D (computed exactly), in 2D and 3D via monte-carlo weighted remapping and a dense mesh.
    * Randoms in cartesian, polar and sphercal polar coordinates.
    * Rotation transformations.
    * Polar coordinate utilities and integration for polar grid to radial profiles.
    * Plotting routine for orthographic projection of unit sphere data.
