# distutils: language = c++
# cython: language_level = 3
from libcpp.vector cimport vector
cdef extern double cpp_convolve(const vector[vector[double] ]& in_a_v, const vector[vector[double] ]& in_b_v, int n_vecs)

ctypedef vector[double] vector_double_t

def cpp_convolve_py(in_a_v: vector[vector_double_t], in_b_v: vector[vector_double_t], n_vecs: int):
    res: float
    res = cpp_convolve(in_a_v, in_b_v, n_vecs)
    return res