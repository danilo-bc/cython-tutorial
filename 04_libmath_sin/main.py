import timeit
import libc_sin
import numpy as np
from math import sin

n_iter = 5000000
x = 3.14151920

from numba import njit
@njit
def f_numba(x):
    return sin(x * x)

print("Python:")
print(timeit.Timer("sin(x * x)", globals=globals()).timeit(number=n_iter)/n_iter)

print("Numba:")
f_numba(x)
print(timeit.Timer("f_numba(x)", globals=globals()).timeit(number=n_iter)/n_iter)

print("Numpy:")
print(timeit.Timer("np.sin(x * x)", globals=globals()).timeit(number=n_iter)/n_iter)

print("Cython:")
print(timeit.Timer("libc_sin.f_cython(x)", globals=globals()).timeit(number=n_iter)/n_iter)
