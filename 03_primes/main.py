import timeit
import primes
import primes_py
import primes_py_cythonized
import primes_cpp

n_iter = 100

assert primes_py.primes_py(1000) == primes_py_cythonized.primes_py_cythonized(1000)
assert primes_py.primes_py(1000) == primes_py.primes_py_njit(1000)
assert primes_py.primes_py(1000) == primes.primes(1000)
assert primes_py.primes_py(1000) == primes_cpp.primes_cpp(1000)

print("Python:")
print(timeit.Timer("primes_py.primes_py(1000)", globals=globals()).timeit(number=n_iter)/n_iter)

print("Python Cythonized:")
print(timeit.Timer("primes_py_cythonized.primes_py_cythonized(1000)", globals=globals()).timeit(number=n_iter)/n_iter)

print("Numba:")
primes_py.primes_py_njit(4)
print(timeit.Timer("primes_py.primes_py_njit(1000)", globals=globals()).timeit(number=n_iter)/n_iter)

print("Cython:")
print(timeit.Timer("primes.primes(1000)", globals=globals()).timeit(number=n_iter)/n_iter)

print("Cython C++:")
print(timeit.Timer("primes_cpp.primes_cpp(1000)", globals=globals()).timeit(number=n_iter)/n_iter)