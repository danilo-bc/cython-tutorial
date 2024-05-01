from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize([
        "print_and_sum_list.pyx"
        ]),
)