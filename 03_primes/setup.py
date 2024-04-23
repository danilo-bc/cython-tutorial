from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize([
        "primes.py",
        "primes_py_cythonized.py",
        "primes_cpp.py"
        ]),
)