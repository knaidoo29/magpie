import numpy as np


def vector_norm(a):
    """Returns the magnitude a vector.

    Parameters
    ----------
    a : array
        Vector a.
    """
    a1, a2, a3 = a[0], a[1], a[2]
    return np.sqrt(a1**2. + a2**2. + a3**2.)


def vector_dot(a, b):
    """Returns the vector dot product.

    Parameters
    ----------
    a : array
        Vector a.
    b : array
        Vector b.
    """
    a1, a2, a3 = a[0], a[1], a[2]
    b1, b2, b3 = b[0], b[1], b[2]
    return a1*b1 + a2*b2 + a3*b3


def vector_cross(a, b):
    """Returns the vector cross product.

    Parameters
    ----------
    a : array
        Vector a.
    b : array
        Vector b.

    Returns
    -------
    s : array
        Cross product vector.
    """
    a1, a2, a3 = a[0], a[1], a[2]
    b1, b2, b3 = b[0], b[1], b[2]
    s1 = a2*b3 - a3*b2
    s2 = a3*b1 - a1*b3
    s3 = a1*b2 - a2*b1
    s = np.array([s1, s2, s3])
    return s
