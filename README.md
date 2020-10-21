# MAGPIE: Monte cArlo weiGhted PIxel rEmapping

MAGPIE is a python module for remapping data from linear cartesian coordinates to
polar coordinates (for 2D) and spherical polar coordinates (for 3D).

Remapping schemes:

- Monte Carlo weights : This uses Monte Carlo for integration to calculate the weights
  that each pixel contributes to the transformed grid. This works very nicely in
  2D but scales poorly for larger data sets.
- Dense Grid : Replace the target grid with a denser grid and assign each point
  in the dense grid the value associated with the center of the pixel. We then rebin
  to the target grid. This is very fast as all computations are deterministic and
  require no for-loops. Assuming the denser grid samples the underlying pixels well
  this should be fairly accurate. This also allows for the simple addition of periodic
  boxes.

## Dependencies

* `numpy`
* `healpy`

## Functions

### Main Remapping Classes

* Monte-carlo weighted pixel remapping:
  - `mc.Box2Ring` : Remaps data on a 2D cartesian grid to a polar coordinate grid with
  a specified center.
  - `mc.Cube2Shell` : Remaps data on 3D cartesian grid to spherical polar coordinates
  with a specified center. Each shell is placed onto a healpix map.

* Dense grid remapping:
  - `dg.Box2Ring` : Remaps data on a 2D cartesian grid to a polar coordinate grid with
  a specified center.
  - `dg.Cube2Shell` : Remaps data on 3D cartesian grid to spherical polar coordinates
  with a specified center. Each shell is placed onto a healpix map. Easy to add periodic
  boxes.

Things to consider:

- The Monte-Carlo weighted remapping is more accurate than the dense grid remapping
  however this accuracy comes with a much longer run time. This however is limited
  to the initial weight calculation. For 2D remapping you could choose to use either
  method however for the 3D case for very large cartesian and spherical polar coordinates
  grids you should use the dense grid approach.
- Boundaries are handled differently. For the Monte-Carlo weighted remapping we assign
  nan's to values outside the boundaries, for the dense grid this is just set to
  0. This is because of how the different methods are implemented.

### Auxillary Functions

* Coordinate transformations and utilities:
  - `coords.cart2polar` : 2D cartesian to polar coordinates.
  - `coords.polar2cart` : 2D polar to cartesian coordinates.
  - `coords.cart2sphere` : 3D cartesian to spherical polar coordinates.
  - `coords.sphere2cart` : 3D spherical polar to cartesian coordinates.
  - `coords.sky_area` : calculates the area of a 'square' patch of sky in steradians.

* Random point generators:
  - `randoms.randoms_polar` : randoms in polar coordinates. Default settings will generate
    randoms inside a unit circle but you can specify the inner and outer radii and
    the angular limits.
  - `randoms.randoms_sky` : randoms on the surface of a unit sphere. Default will generate
    randoms on the full sky, however you can limit the latitudinal and longitudinal
    angles to a 'square' patch.
  - `randoms.randoms_healpix_pixel` : randoms inside a healpix pixel.
  - `randoms.randoms_sphere_r` : the radial coordinates for randoms in a sphere or shell.
  - `randoms.randoms_sphere` : randoms in spherical polar coordinates. Default will generate
    randoms inside a unit sphere. Can be isolated to a shell and restricted to
    certain angles on the sky.

* Rotation functions:
  - `rotate.rotate_polar` : rotates data on a polar coordinate grid.

* `utils.progress_bar` : progress_bar for for-loop progress.

## Installation

Clone the github repository:

```
git clone https://github.com/knaidoo29/magpie
```

To install using pip:

```
cd magpie
pip install -e . [--user]
```

or use setup:

```
cd magpie
python setup.py build
python setup.py install
```

## Usage

Examples are provided as jupyter notebooks in the tutorial folder.

## Citing

Please provide a link to the github repository.

## Support

If you have any issues with the code or want to suggest ways to improve it please open a new issue ([here](https://github.com/knaidoo29/magpie/issues)) or (if you don't have a github account)
email _krishna.naidoo.11@ucl.ac.uk_.
