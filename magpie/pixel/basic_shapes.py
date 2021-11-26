import numpy as np

from .. import coords


def get_square(xmin, xmax, ymin, ymax, steps=40):
    """Returns the coordinates of the perimeter of a rectangle.

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
    steps : int, optional
        Number of divisions across each line segment, default = 4.

    Returns
    -------
    x, y : array
        Perimeter coordinates of a rectangle.
    """
    assert steps % 4 == 0 and steps > 0, \
        "Steps must be a multiple of 4 and greater than 0."
    steps1 = int(steps/4)
    steps2, steps3, steps4 = steps1, steps1, steps1
    x = []
    y = []
    xx = np.linspace(xmin, xmax, steps1)
    yy = np.ones(steps1)*ymin
    x, y = xx, yy
    xx = np.ones(steps2)*xmax
    yy = np.linspace(ymin, ymax, steps2)
    x = np.concatenate([x, xx])
    y = np.concatenate([y, yy])
    xx = np.linspace(xmax, xmin, steps3)
    yy = np.ones(steps3)*ymax
    x = np.concatenate([x, xx])
    y = np.concatenate([y, yy])
    xx = np.ones(steps4)*xmin
    yy = np.linspace(ymax, ymin, steps4)
    x = np.concatenate([x, xx])
    y = np.concatenate([y, yy])
    return x, y


def get_arc(radius, phimin=0., phimax=2.*np.pi, center=[0., 0.], steps=10):
    """Returns the coordinates of the arc of a circle, default settings will
    return the coordinates along a complete circle.

    Parameters
    ----------
    radius : float
        Radius of the circle.
    phimin : float, optional
        Minimum phi value, default=0.
    phimax : float, optional
        Maximum phi value, default=2pi.
    center : list, optional
        Central x and y coordinates for the arc.
    steps : int, optional
        The number of points along the arc curve.

    Returns
    -------
    x, y : array
        Coordinates along the arc of a circle.
    """
    phi = np.linspace(phimin, phimax, steps)
    r = np.ones(steps)*radius
    x, y = coords.polar2cart(r, phi, center=center)
    return x, y


def get_disc(rmin=0., rmax=1., phimin=0., phimax=2.*np.pi,
             center=[0., 0.], steps=40):
    """Returns the coordinates of a disc segment.

    Parameters
    ----------
    rmin : float, optional
        Minimum radial value, default=0.
    rmax : float, optional
        Maximum radial value, default=1.
    phimin : float, optional
        Minimum phi value, default=0.
    phimax : float, optional
        Maximum phi value, default=2pi.
    center : list, optional
        Central x and y coordinates for the arc.
    steps : int, optional
        The number of points along the arc curve.

    Returns
    -------
    x, y : array
        Coordinates along the arc of a circle.
    """
    r, phi = get_square(rmin, rmax, phimin, phimax, steps=steps)
    x, y = coords.polar2cart(r, phi, center=center)
    return x, y


def get_box(xmin, xmax, ymin, ymax, zmin, zmax, steps=120,
            return_nearest=False, center=[0., 0., 0.]):
    """Returns 3D coordinates for a box.

    Parameters
    ----------
    xmin : float
        Minimum x value.
    xmax : float
        Maximum x value.
    ymin : float
        Minimum y value.
    ymax : float
        Maximum y value.
    zmin : float
        Minimum z value.
    zmax : float
        Maximum z value.
    steps : int, optional
        Number of divisions in each line element.
    return_nearest : bool, optional
        If True only the lines for the nearest or visible faces from a defined
        center will be outputed.
    center : list, optional
        Coordinate center used for return_nearest=True

    Returns
    -------
    x, y, z : array
        Coordinates of the box edges.
    """
    assert steps % 12 == 0 and steps > 0, \
        "steps must be a multiple of 12 and greater than 0."
    steps1 = int(steps/12)
    xmin_arr = xmin*np.ones(steps1)
    xmax_arr = xmax*np.ones(steps1)
    ymin_arr = ymin*np.ones(steps1)
    ymax_arr = ymax*np.ones(steps1)
    zmin_arr = zmin*np.ones(steps1)
    zmax_arr = zmax*np.ones(steps1)
    x_arr = np.linspace(xmin, xmax, steps1)
    y_arr = np.linspace(ymin, ymax, steps1)
    z_arr = np.linspace(zmin, zmax, steps1)
    x = np.array([x_arr, x_arr, xmin_arr, xmax_arr, x_arr, x_arr, xmin_arr,
                  xmax_arr, xmin_arr, xmax_arr, xmin_arr, xmax_arr])
    y = np.array([ymin_arr, ymax_arr, y_arr, y_arr, ymin_arr, ymax_arr, y_arr,
                  y_arr, ymin_arr, ymin_arr, ymax_arr, ymax_arr])
    z = np.array([zmin_arr, zmin_arr, zmin_arr, zmin_arr, zmax_arr, zmax_arr,
                  zmax_arr, zmax_arr, z_arr, z_arr, z_arr, z_arr])
    if return_nearest is True:
        corners = np.array([[xmin, ymin, zmin], [xmin, ymin, zmax],
                            [xmin, ymax, zmin], [xmin, ymax, zmax],
                            [xmax, ymin, zmin], [xmax, ymin, zmax],
                            [xmax, ymax, zmin], [xmax, ymax, zmax]])
        xc, yc, zc = corners[:, 0], corners[:, 1], corners[:, 2]
        remove_corner = []
        for i in range(0, len(corners)):
            xx = np.linspace(0., 1., 100)*(xc[i] - center[0]) + center[0]
            yy = np.linspace(0., 1., 100)*(yc[i] - center[1]) + center[1]
            zz = np.linspace(0., 1., 100)*(zc[i] - center[2]) + center[2]
            condition = np.where((xx > xmin) & (xx < xmax) & (yy > ymin) &
                                 (yy < ymax) & (zz > zmin) & (zz < zmax))[0]
            if len(condition) == 0:
                remove_corner.append(False)
            else:
                remove_corner.append(True)
        xnew = []
        ynew = []
        znew = []
        for i in range(0, len(x)):
            x1, y1, z1 = x[i][0], y[i][0], z[i][0]
            x2, y2, z2 = x[i][-1], y[i][-1], z[i][-1]
            dist1 = np.sqrt((xc - x1)**2. + (yc - y1)**2. + (zc - z1)**2.)
            dist2 = np.sqrt((xc - x2)**2. + (yc - y2)**2. + (zc - z2)**2.)
            remove_corner1 = remove_corner[np.argmin(dist1)]
            remove_corner2 = remove_corner[np.argmin(dist2)]
            if remove_corner1 is True or remove_corner2 is True:
                remove = True
            else:
                remove = False
            if remove is False:
                xnew.append(x[i])
                ynew.append(y[i])
                znew.append(z[i])
        xnew = np.array(xnew)
        ynew = np.array(ynew)
        znew = np.array(znew)
        x, y, z = xnew, ynew, znew
    return x, y, z
