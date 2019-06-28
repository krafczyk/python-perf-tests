CXXFLAGS := -Wall -Werror -fPIC

all: fib_clib/libfib_clib.so fib_clib/libfib_clibO3.so

fib_clib/libfib_clib.so: fib_clib/imp.cpp
	g++ -O0 $(CXXFLAGS) -shared $< -o $@

fib_clib/libfib_clibO3.so: fib_clib/imp.cpp
	g++ -O3 $(CXXFLAGS) -shared $< -o $@
