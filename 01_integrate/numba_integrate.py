import cython # just to copy and paste code from integrate, has no effect in this file!!
from numba import njit

@njit
def jit_f(x: cython.double):
    return x ** 2 - x

@njit
def jit_integrate_f(a: cython.double, b: cython.double, N: cython.int):
    i: cython.int
    s: cython.double
    dx: cython.double
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += jit_f(a + i * dx)
    return s * dx