import timeit
import fib
import fib_py
n_iter = 50

print("Python:")
print(timeit.Timer("fib_py.fib_py(2000)", globals=globals()).timeit(number=n_iter)/n_iter)

print("Cython:")
print(timeit.Timer("fib.fib(2000)", globals=globals()).timeit(number=n_iter)/n_iter)