all: operations.cpp cpp_operations.pyx
	python setup.py build_ext --inplace

clean:
	rm -f cpp_operations.cpp
	rm -f *.cpython*
	rm -rf build