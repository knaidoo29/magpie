====================================
Monte cArlo weiGhted PIxel rEmapping
====================================

.. image:: https://readthedocs.org/projects/magpie-doc/badge/?version=latest
    :target: https://magpie-doc.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


+---------------+-----------------------------------------+
| Author        | Krishna Naidoo                          |
+---------------+-----------------------------------------+
| Version       | 0.2.1                                   |
+---------------+-----------------------------------------+
| Repository    | https://github.com/knaidoo29/magpie     |
+---------------+-----------------------------------------+
| Documentation | https://magpie-doc.readthedocs.io/      |
+---------------+-----------------------------------------+

.. warning ::
  MAGPIE is currently in development. Functions and classes may change. Use with caution.

Introduction
============

MAGPIE is a python module for remapping bins (in 1D), pixels (in 2D) and cells (in 3D)
into different coordinate systems. The package will enable data to be remapped
from cartesian to polar coordinates, cartesian to spherical polar coordinates
and will enable rotations of these systems.

When carrying out coordinate transformations we typically take the center of the
pixel or cell and apply the transform without considering the surface area of the
pixel (or volume of the cell). In MAGPIE this is taken into account by applying two
remapping schemes. The first weights pixels to a new coordinate grid using monte-carlo
integration. The second uses a dense grid (denser than the new coordinate grid) which
is rebinned to the target coordinate grid. In both cases we sample the surface area
or volume of the new coordinate pixels to accurately remap the data. The monte-carlo
method is more accurate but scales poorly to 3D. For 2D this scheme will work very
well even for moderately large datasets. The dense grid method, while less accurate,
is very fast and should be used for large data sets and all 3D transformations.
In 1D these are computed exactly without requiring the approximate schemes above.

.. warning ::
  MPI functionality is currently unavailable but the plan will be to implement this
  using mpi4py and an additional library MPIutils which will handle all of the MPI
  enabled functions.

Contents
========

.. toctree::
   :maxdepth: 2

   remap_index
   randoms_index
   api


Dependencies
============

MAGPIE is being developed in Python 3.8 but should work on all versions >3.4. MAGPIE
is written mostly in python but with some heavy computation carried out in Fortran.
Compiling the Fortran source code will require the availability of a fortran compiler
usually gfortran (which comes with gcc).

The following Python modules are required.

* `numpy <http://www.numpy.org/>`_
* `scipy <https://scipy.org/>`_
* `healpy <https://healpy.readthedocs.io/>`_

If you want to run with MPI you will need the following:

* `mpi4py <https://mpi4py.readthedocs.io/en/stable/>`_
* `MPIutils <https://github.com/knaidoo29/MPIutils>`_

For testing you will require `nose <https://nose.readthedocs.io/en/latest/>`_ or
`pytest <http://pytest.org/en/latest/>`_ .


Installation
============

SHIFT can be installed by cloning the github repository::

    git clone https://github.com/knaidoo29/magpie.git
    cd magpie
    python setup.py build
    python setup.py install

Once this is done you should be able to call MAGPIE from python:

.. code-block:: python

    import magpie

Support
=======

If you have any issues with the code or want to suggest ways to improve it please
open a new issue (`here <https://github.com/knaidoo29/magpie/issues>`_) or
(if you don't have a github account) email krishna.naidoo.11@ucl.ac.uk.


Version History
===============

**Version 0.0**:

  * Randoms in a variety of coordinate systems: cartesian, polar, spherical and from an input PDF/CDF.

  * Remapping procedures in 1D (exact and analytical), 2D (monte-carlo and grid based methods) for cartesian, polar and the surface of a sphere and lastly in 3D (monte-carlo and grid based methods) cartesian and spherical polar coordinates.

  * Plotting routines.
