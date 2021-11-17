=====
Remap
=====

Remapping data from one coordinate system mesh to another can play a critical role
in data science. Converting one dimensional data, image-like data in two dimensions
and three dimensional mesh data into another coordinate systems can be critical in
enabling certain analysis pipelines to be calculated and on a more fundamental
level enable better intuitive understanding of certain phenomena. Typically we
assume that data provided on a grid can be defined by the cells (bins in 1D and
pixels in 2D) center and map those central positions into a new coordinate system.
However, this fails to take into account the pixel's volume (length in 1D and area
in 2D) and can lead to some strange artifacts (such as empty pixels in the new
coordinate mesh). A possible solution to this problem is to use interpolation however
while interpolation works well for theoretically generated data, for measured data
this makes the implicit assumption that data measured and binned in a cell is
equivalent to the value at the cells center. In general this assumption is not hugely
problematic but can lead to some issues particularly when the cells are integrated
values across the cell. In ``magpie`` we take a different approach, we consider each
pixels volume and map to another coordinate system mesh by taking the volume-weighted
mean of overlapping pixels in the original coordinate system. This is achieved through
two methods, the first uses monte carlo integration to determine the weights but
for large data sets this can be slow so a second scheme approximates these weights
by using a higher resolution mesh.

Theory
======

Remapping data :math:`d` (defined in coordinate system :math:`X`) to a new coordinate
system :math:`Y` is calculated by taking the weighted mean,

.. math::

  \tilde{d}(Y_{j}) = \frac{\sum_{i=1}^{N}w_{j}(X_{i})d(X_{i})}{\sum_{i=1}^{N}w_{j}(X_{i})},

where :math:`\tilde{d}` is :math:`d` mapped onto coordinate system :math:`Y`.

Tutorial
========
