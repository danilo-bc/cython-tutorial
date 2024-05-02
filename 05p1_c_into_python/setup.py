from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    ext_modules=cythonize([
        Extension("cpp_hello", ["cpp_hello.pyx", "hello.cpp"])
        ]),
)
