import numpy as np
import copy
import pytest

__all__ = ['gauss', 'zeromat', 'matmul']


def gauss(a, b):
    """
    Given two matrices, `a` and `b`, with `a` square, the determinant
    of `a` and a matrix `x` such that a*x = b are returned.
    If `b` is the identity, then `x` is the inverse of `a`.

    Parameters
    ----------
    a : np.array or list of lists
        'n x n' array
    b : np. array or list of lists
        'm x n' array

    Examples
    --------
    >>> a = [[2, 0, -1], [0, 5, 6], [0, -1, 1]]
    >>> b = [[2], [1], [2]]
    >>> det, x = gauss(a, b)
    >>> det
    22.0
    >>> x
    [[1.5], [-1.0], [1.0]]
    >>> A = [[1, 0, -1], [-2, 3, 0], [1, -3, 2]]
    >>> I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    >>> Det, Ainv = gauss(A, I)
    >>> Det
    3.0
    >>> Ainv
    [[2.0, 1.0, 1.0],
    [1.3333333333333333, 1.0, 0.6666666666666666],
    [1.0, 1.0, 1.0]]

    Notes
    -----
    See https://en.wikipedia.org/wiki/Gaussian_elimination for further details.
    """
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    n = len(a)
    p = len(b[0])
    det = np.ones(1, dtype=np.float64)
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
            det = -det

        for j in range(i + 1, n):
            t = a[j][i]/a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t*a[i][k]
            for k in range(p):
                b[j][k] -= t*b[i][k]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                b[i][k] -= t*b[j][k]
        t = 1/a[i][i]
        det *= a[i][i]
        my_det = det[0]
        for j in range(p):
            b[i][j] *= t
    return my_det, b
#a = [[1, 9.8, -1], [-2, 3, 0], [1, -3, 2]]
#b = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

#print(gauss(a,b))

def zeromat(p, q):
    """
    Given matirx size, `p` and `q`, return a p*w null matrix

    Parameters
    ----------
    p : int
        row size
    q : int
        column size

    Examples
    --------
    >>> p = 3
    >>> q = 3
    >>> a = zeromat(p, q)
    >>> a
    [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

    Notes
    -----
    See https://en.wikipedia.org/wiki/Zero_matrix for further details.
    """
    return [[0]*q for i in range(p)]

def matmul(a, b):
    """
    Given two matrices, `a` and `b`,
    return the matrix multiplication 'a*b'

    Parameters
    ----------
    a : np.array or list of lists
        'n x p' array
    b : np. array or list of lists
        'p1 x q' array

    Examples
    --------
    >>> a = [[2, 0, -1], [0, 5, 6], [0, -1, 1]]
    >>> b = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    >>> c = matmul(a, b)
    >>> c
    [[2, 0, -1],
    [0, 5, 6],
    [0, -1, 1]]

    Notes
    -----
    resource: https://en.wikipedia.org/wiki/Matrix_multiplication
    """
    n, p = len(a), len(a[0])
    p1, q = len(b), len(b[0])
    if p != p1:
        raise ValueError("Incompatible dimensions")
    c = zeromat(n, q)
    for i in range(n):
        for j in range(q):
            c[i][j] = sum(a[i][k]*b[j][k] for k in range(p))
    return c

if __name__ == "__main__":
    import doctest
    doctest.testmod()
