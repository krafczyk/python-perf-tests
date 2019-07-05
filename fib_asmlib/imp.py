import ctypes

libfib_asmlib = ctypes.cdll.LoadLibrary("fib_asmlib/libfib_asmlib.so")
libfib_asmlib.iterative.restype = ctypes.c_longlong
libfib_asmlib.iterative.argtypes = [ctypes.c_longlong]
libfib_asmlib.iterative_short.restype = ctypes.c_longlong
libfib_asmlib.iterative_short.argtypes = [ctypes.c_longlong]

def iterative(n):
    return int(libfib_asmlib.iterative(n))

def iterative_short(n):
    return int(libfib_asmlib.iterative_short(n))
