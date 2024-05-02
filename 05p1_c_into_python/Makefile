all: hello.cpp cpp_hello.pyx
	python setup.py build_ext --inplace

clean:
	rm -f cpp_hello.cpp
	rm -f *.cpython*
	rm -rf build