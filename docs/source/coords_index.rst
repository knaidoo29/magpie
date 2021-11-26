======
Coords
======

Conventions
===========

All angular coordinates are defined in radians.

Polar Coordinates
-----------------

Polar coordinates are related to 2D cartesian coordinates by the relations

.. math::

  & x = r\cos(\phi) + x_{0},\\
  & y = r\sin(\phi) + y_{0},

where :math:`x_{0}` and :math:`y_{0}` define the center of the polar coordinate
grid. The polar coordinates :math:`r` lies in the range :math:`[0, \infty)`
while :math:`\phi` lies in the range :math:`[0, 2\pi)`. The conversion from 2D
cartesian coordinates to polar is given by

.. math::

  & r = \sqrt{(x-x_{0})^{2} + (y-y_{0})^{2}},\\
  & \phi = \arctan \left(\frac{y-y_{0}}{x-x_{0}}\right).

.. note::

  This means :math:`\phi=0` lies along the x-axis i.e. y=0.

Spherical Polar Coordinates
---------------------------


API
===

.. toctree::

    coords_func_list
