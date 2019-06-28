CXXFLAGS := -Wall -Werror

all: fib_clib/libfib_clib.so fib_clib/libfib_clibO3.so

test: fib_clib/test.exe fib_clib/test.s

fib_clib/libfib_clib.so: fib_clib/imp.cpp
	g++ -O0 $(CXXFLAGS) -fPIC -shared $< -o $@

fib_clib/libfib_clibO3.so: fib_clib/imp.cpp
	g++ -O3 $(CXXFLAGS) -fPIC -shared $< -o $@

fib_clib/test.exe: fib_clib/test.cpp fib_clib/imp.cpp
	g++ -g -O0 $(CXXFLAGS) -I fib_clib $< -o $@

fib_clib/test.s: fib_clib/test.cpp fib_clib/imp.cpp
	g++ -g -O0 $(CXXFLAGS) -I fib_clib -S $< -o $@
