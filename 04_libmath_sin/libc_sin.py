import cython
from cython.cimports.libc.math import sin

@cython.cfunc
def f(x: cython.double) -> cython.double:
    return sin(x * x)

def f_cython(x: cython.double) -> cython.double:
    return f(x)