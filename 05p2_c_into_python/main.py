import time
import random
import numpy as np
from numba import njit
from cpp_operations import cpp_convolve_py

n_vecs = 128 #at least 2
vec_size = 128

def py_convolve(in_a, in_b, n_vecs):
    accum = 0
    for i in range(n_vecs):
        conv_res   = np.convolve(in_a[i,:], in_b[i,:])
        even_part  = conv_res[2::2]
        odd_part   = conv_res[1::2]
        accum     += np.sum(even_part - odd_part)
    return accum

@njit
def njit_convolve(in_a, in_b, n_vecs):
    accum = 0
    for i in range(n_vecs):
        conv_res   = np.convolve(in_a[i,:], in_b[i,:])
        even_part  = conv_res[2::2]
        odd_part   = conv_res[1::2]
        accum     += np.sum(even_part - odd_part)
    return accum

# Utility
def scientific_time(time_in_seconds):
    """String of time converted to closest scientific representation

    Args:
        time_in_seconds (double): time in seconds

    Returns:
        str: Converted time. e.g., 0.005 => 5 ms
    """
    powers = [(1e-12, 'ps'), (1e-9, 'ns'), (1e-6, 'μs'), (1e-3, 'ms'), (1, 's'), (60, 'min'), (3600, 'hr'), (86400, 'day')]
    
    closest_power = min(powers, key=lambda x: abs(time_in_seconds - x[0]))
    return f"{time_in_seconds / closest_power[0]:.3f} {closest_power[1]}"

## Benchmark
i_data_a = np.random.random([n_vecs, vec_size])
i_data_b = np.random.random([n_vecs, vec_size])

print("Python:")
start_time = time.perf_counter()
py_res = py_convolve(i_data_a, i_data_b, n_vecs)
elapsed_time = time.perf_counter() - start_time
print(f"\tTotal time:\t\t{scientific_time(elapsed_time)}")
print(f"\tMean time per vector:\t{scientific_time(elapsed_time / n_vecs)}")

print("Numba:")
njit_convolve(i_data_a[0:1,:], i_data_b[0:1,:], 2) #warm up JIT
start_time = time.perf_counter()
njit_res = njit_convolve(i_data_a, i_data_b, n_vecs)
elapsed_time = time.perf_counter() - start_time
print(f"\tTotal time:\t\t{scientific_time(elapsed_time)}")
print(f"\tMean time per vector:\t{scientific_time(elapsed_time / n_vecs)}")

print("Cython C++:")
start_time = time.perf_counter()
cpp_res = cpp_convolve_py(i_data_a, i_data_b, n_vecs)
elapsed_time = time.perf_counter() - start_time
print(f"\tTotal time:\t\t{scientific_time(elapsed_time)}")
print(f"\tMean time per vector:\t{scientific_time(elapsed_time / n_vecs)}")

if py_res == njit_res == cpp_res:
    print(f"\nResults are equal between approaches")
else:
    print("\nResults are different:")
    print(f"Python:\t\t{py_res}")
    print(f"Numba:\t\t{njit_res}")
    print(f"Cython C++:\t{cpp_res}")
