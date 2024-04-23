all: primes.py
	python setup.py build_ext --inplace

clean:
	rm -f primes.c*
	rm -f primes_py_cythonized.c*
	rm -f primes_cpp.cpp
	rm -f *.cpython*
	rm -rf build