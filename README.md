# MAGPIE: Monte cArlo weiGhted PIxel rEmapping

MAGPIE is a python module for remapping data from linear cartesian coordinates to
polar coordinates (for 2D) and spherical polar coordinates (for 3D). The remapping
uses monte carlo integration for calculating the weights each pixel contributes to
the transformed grid.

## Dependencies

* `numpy`
* `matplotlib`
* `healpy`

## To-do

* 3D grid to spherical polar coordinate grid (normal and healpix version).

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

## Citing

Please provide a link to the github repository.

## Support

If you have any issues with the code or want to suggest ways to improve it please open a new issue ([here](https://github.com/knaidoo29/magpie/issues)) or (if you don't have a github account)
email _krishna.naidoo.11@ucl.ac.uk_.
