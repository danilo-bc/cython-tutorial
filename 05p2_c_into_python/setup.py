from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    ext_modules=cythonize([
        Extension("cpp_operations", ["cpp_operations.pyx", "operations.cpp"])
        ]),
)
