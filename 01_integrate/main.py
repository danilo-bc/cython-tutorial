import timeit
from integrate import integrate_f
from numba_integrate import jit_integrate_f

n_iter = 500

a = 1
b = 10
N = 10000

print("Python:")
integrate_f(a, b, N)
print(timeit.Timer("integrate_f(a, b, N)", globals=globals()).timeit(number=n_iter)/n_iter)

print("Numba:")
jit_integrate_f(a, b, N)
print(timeit.Timer("jit_integrate_f(a, b, N)", globals=globals()).timeit(number=n_iter)/n_iter)