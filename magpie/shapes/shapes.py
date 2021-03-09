import numpy as np


def get_box(xmin, xmax, ymin, ymax, divisions=1):
    """Returns the coordinates of the perimeter of a box.

    Parameters
    ----------
    xmin : float
        Minimum x-value.
    xmax : float
        Maximum x-value.
    ymin : float
        Minimum y-value.
    ymax : float
        Maximum y-value.
    divisions : int, optional
        Number of divisions across each line segment.
    """
    x = []
    y = []
    xx = np.linspace(xmin, xmax, divisions+1)
    yy = np.ones(divisions+1)*ymin
    x = xx[:-1]
    y = yy[:-1]
    xx = np.ones(divisions+1)*xmax
    yy = np.linspace(ymin, ymax, divisions+1)
    x = np.concatenate([x, xx[:-1]])
    y = np.concatenate([y, yy[:-1]])
    xx = np.linspace(xmax, xmin, divisions+1)
    yy = np.ones(divisions+1)*ymax
    x = np.concatenate([x, xx[:-1]])
    y = np.concatenate([y, yy[:-1]])
    xx = np.ones(divisions+1)*xmin
    yy = np.linspace(ymax, ymin, divisions+1)
    x = np.concatenate([x, xx])
    y = np.concatenate([y, yy])
    return x, y


def get_circle(radius, center=[0., 0.], length=100):
    """Returns the coordinates of the perimeter of a box.

    Parameters
    ----------
    radius : float
        Radius of the circle.
    center : list, optional
        Central x and y coordinate of the circle.
    length : int, optional
        Length of the circle coordinates.
    """
    phi = np.zeros(length)
    phi[:-1] = np.linspace(0., 2.*np.pi, length)[:-1]
    r = np.ones(length)*radius
    x = r*np.cos(phi)
    y = r*np.sin(phi)
    x += center[0]
    y += center[0]
    return x, y
