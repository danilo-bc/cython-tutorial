from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize([
        "libc_sin.py"
        ]),
)