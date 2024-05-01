# distutils: language=c++

from libcpp.vector cimport vector

def print_list(vector[double] i_list):
    cdef int i
    for i in range(len(i_list)):
        print(i_list[i])
    
    return

def print_sum(vector[double] i_list):
    cdef int i
    print(sum(i_list))
