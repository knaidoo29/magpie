import numpy as np
from numba import njit


@njit
def dot3by3(a, b):
    """
    Computes the dot product of two 3x3 matrices.
    
    Parameters
    ----------
    a : array (1D, length 9)
        First 3x3 matrix stored in row-major order.
    b : array (1D, length 9)
        Second 3x3 matrix stored in row-major order.
    
    Returns
    -------
    c : array (1D, length 9)
        Resulting 3x3 matrix stored in row-major order.
    """
    c = np.zeros(9, dtype=np.float64)
    
    c[0] = a[0]*b[0] + a[1]*b[3] + a[2]*b[6]
    c[1] = a[0]*b[1] + a[1]*b[4] + a[2]*b[7]
    c[2] = a[0]*b[2] + a[1]*b[5] + a[2]*b[8]

    c[3] = a[3]*b[0] + a[4]*b[3] + a[5]*b[6]
    c[4] = a[3]*b[1] + a[4]*b[4] + a[5]*b[7]
    c[5] = a[3]*b[2] + a[4]*b[5] + a[5]*b[8]

    c[6] = a[6]*b[0] + a[7]*b[3] + a[8]*b[6]
    c[7] = a[6]*b[1] + a[7]*b[4] + a[8]*b[7]
    c[8] = a[6]*b[2] + a[7]*b[5] + a[8]*b[8]
    
    return c