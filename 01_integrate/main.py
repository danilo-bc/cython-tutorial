import timeit
from integrate import integrate_f

n_iter = 500

a = 1
b = 10
N = 10000

print("Python:")
print(timeit.Timer("integrate_f(a, b, N)", globals=globals()).timeit(number=n_iter)/n_iter)