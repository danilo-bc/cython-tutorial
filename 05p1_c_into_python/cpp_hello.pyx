# distutils: language = c++
# cython: language_level = 3
cpdef extern void hello_from_cpp()

def hello_from_cpp_wrapper():
    hello_from_cpp()