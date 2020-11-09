# MAGPIE: Monte cArlo weiGhted PIxel rEmapping

Author:         Krishna Naidoo                          
Version:        1.0.0                               
Homepage:       https://github.com/knaidoo29/magpie    
Documentation:  n/a

MAGPIE is a python module for remapping pixels (in 2D) and cells (in 3D) into different
coordinate systems. The package will enable data to be remapped from cartesian to
polar coordinates, cartesian to spherical polar coordinates and will enable rotations
of these systems.

When carrying out coordinate transformations we typically take the center of the
pixel or cell and apply the transform without considering the surface area of the
pixel (or volume of the cell). In magpie this is taken into account by applying two
remapping schemes. The first weights pixels to a new coordinate grid using monte-carlo
integration. The second uses a dense grid (denser than the new coordinate grid) which
is rebinned to the target coordinate grid. In both cases we sample the surface area
or volume of the new coordinate pixels to accurately remap the data. The monte-carlo
method is more accurate but scales poorly to 3D. For 2D this scheme will work very
well even for moderately large datasets. The dense grid method, while less accurate,
is very fast and should be used for large data sets and all 3D transformations.

## Dependencies

* `Python 3`
* `numpy`
* `healpy`

## Functions

#### Main Remapping Classes

* Monte-carlo weighted pixel remapping:
  - `mc.Box2Ring`: Remaps data on a 2D cartesian grid to a polar coordinate grid with
  a specified center.
  - `mc.Cube2Shell`: Remaps data on 3D cartesian grid to spherical polar coordinates
  with a specified center. Each shell is placed onto a healpix map.

* Dense grid remapping:
  - `dg.Box2Ring`: Remaps data on a 2D cartesian grid to a polar coordinate grid with
  a specified center.
  - `dg.Cube2Shell`: Remaps data on 3D cartesian grid to spherical polar coordinates
  with a specified center. Each shell is placed onto a healpix map. Easy to add periodic
  boxes.

Things to consider:

- The Monte-Carlo weighted remapping is more accurate than the dense grid remapping
  however this accuracy comes with a much longer run time. However, this is limited
  only to the initial weight calculation, remapping once this has been completed
  is fairly fast. For 2D remapping you could choose to use either method however
  for the 3D case, unless the grid is very small, it is recommended you use the
  dense grid approach.
- Boundaries are handled differently for each approach. For the Monte-Carlo weighted
  remapping we assign nan's to values outside the boundaries, for the dense grid this
  is just set to 0. This is because of how the different methods are implemented.

#### Additional Functions

* Coordinate transformations and utilities:
  - `coords.cart2polar`: 2D cartesian to polar coordinates.
  - `coords.polar2cart`: 2D polar to cartesian coordinates.
  - `coords.cart2sphere`: 3D cartesian to spherical polar coordinates.
  - `coords.sphere2cart`: 3D spherical polar to cartesian coordinates.
  - `coords.sky_area`: calculates the area of a 'square' patch of sky in steradians.

* Polar coordinate grid to 1D radial profiles:
  - `polar.get_polar_area2d`: Returns the area of each pixel in the polar coordinate grid.
  - `polar.get_pixarea`: Returns the area of each pixel in the cartesian grid.
  - `polar.polar2radial`: Converts a 2D polar coordinate grid to its 1D radial profile.
  
* Random point generators:
  - `randoms.randoms_polar`: randoms in polar coordinates. Default settings will generate
    randoms inside a unit circle but you can specify the inner and outer radii and
    the angular limits.
  - `randoms.randoms_sky`: randoms on the surface of a unit sphere. Default will generate
    randoms on the full sky, however you can limit the latitudinal and longitudinal
    angles to a 'square' patch.
  - `randoms.randoms_healpix_pixel`: randoms inside a healpix pixel.
  - `randoms.randoms_sphere_r`: the radial coordinates for randoms in a sphere or shell.
  - `randoms.randoms_sphere`: randoms in spherical polar coordinates. Default will generate
    randoms inside a unit sphere. Can be isolated to a shell and restricted to
    certain angles on the sky.

* Rotation functions:
  - `rotate.rotate_polar`: rotates data on a polar coordinate grid.

* Utility functions:
  - `utils.progress_bar`: progress_bar for for-loop progress.

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
