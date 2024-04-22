from setuptools import setup
from Cython.Build import cythonize

setup(
    name="Integrate function",
    ext_modules=cythonize("integrate.py"),
)