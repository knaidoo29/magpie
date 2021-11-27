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
two methods, the first uses monte carlo (MC) integration to determine the weights but
for large data sets this can be slow so a second scheme approximates these weights
by using a higher resolution (HR) mesh.

Theory
======

Remapping
---------

Remapping data :math:`d` (defined in coordinate system :math:`X`) to a new coordinate
system :math:`Y` is calculated by taking the weighted mean,

.. math::

  \tilde{d}(Y_{j}) = \sum_{i=1}^{N}w(X_{i}, Y_{j})d(X_{i}),

where :math:`\tilde{d}` is :math:`d` mapped onto coordinate system :math:`Y` and
:math:`i` and :math:`j` indicate pixels in  :math:`X` and :math:`Y` respectively.
The weights :math:`w(X, Y)` are given by

.. math::

  w(X, Y) = \frac{A(X\cap Y)}{A(Y)},

where :math:`A(Y)` is the area (length in 1D and volume in 3D) of pixel Y and :math:`A(X\cap Y)`
is the area of the overlapping region for pixels X and Y. For variance we can use
propagation of errors to determine the variance on the remapped coordinate system
although note we assume covariant terms are zero. The remapped variance is given by

.. math::

  \tilde{\Delta d}^{2}(Y_{j}) = \sum_{i=1}^{N}U(X_{i}, Y_{j})w^{2}(X_{i}, Y_{j})\Delta d^{2}(X_{i}).

Note, the variance for a subset of :math:`X` called :math:`s` is given by the relation

.. math::

  \Delta d^{2} (s) = \frac{A(s)}{A(X)}\Delta d^{2}(X),

this assumes that the variance observed in a bin is actually the standard error on
the mean for that bin. The above relation shows that dividing by the area gives a
normalised variance,

.. math::

  \delta d^{2}(X) = \frac{1}{A(X)}\Delta d^{2}(X),

and it follows for :math:`\tilde{\delta d}(Y)\equiv\delta d(X)` for constant variance
that :math:`U(X_{i}, Y_{j})=A(X_{i})/A(Y_{j})` which means,

.. math::

  \tilde{\Delta d}^{2}(Y_{j}) = \sum_{i=1}^{N}\frac{A(X_{i})}{A(Y_{j})}w^{2}(X_{i}, Y_{j})\Delta d^{2}(X_{i}).

Weight Calculation
------------------

Monte-Carlo Method
^^^^^^^^^^^^^^^^^^

Weights are computed by monte carlo integration -- random points are distributed
equally in each pixel :math:`Y` and the weights are simply the normalised counts
which fall into pixels in :math:`X`.

Higher-Resolution Method
^^^^^^^^^^^^^^^^^^^^^^^^

A higher resolution mesh, determined by some input integer factor :math:`N_{H}`,
is constructed. This means for the new coordinate system :math:`Y` there are :math:`N_{H}`
HR pixels in each of the coordinate dimensions. The weights are simply given by

.. math::

  w(X_{i}, Y_{j}) = \frac{1}{A(Y_{j})}\sum_{k=1}^{N_{H}^{D}} A(y_{k})S(y_{k}, X_{i})

where :math:`D` is the dimension of the coordinate system, :math:`y` indicates pixels
in the higher resolution mesh and :math:`S(y_{k}, X_{i})=1` if the pixel center for
:math:`y` is within :math:`X_{i}` and :math:`0` otherwise.

Tutorial
========

API
===


.. toctree::

    remap_func_list
