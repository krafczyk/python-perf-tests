import ctypes

libfib_clib = ctypes.cdll.LoadLibrary("fib_clib/libfib_clib.so")
libfib_clib.recursive_dynamic.restype = ctypes.c_longlong
libfib_clib.recursive_dynamic.argtypes = [ctypes.c_longlong]
libfib_clib.iterative.restype = ctypes.c_longlong
libfib_clib.iterative.argtypes = [ctypes.c_longlong]
libfib_clib.iterative_asm.restype = ctypes.c_longlong
libfib_clib.iterative_asm.argtypes = [ctypes.c_longlong]
libfib_clib.power_matrix.restype = ctypes.c_longlong
libfib_clib.power_matrix.argtypes = [ctypes.c_longlong]

libfib_clibO3 = ctypes.cdll.LoadLibrary("fib_clib/libfib_clibO3.so")
libfib_clibO3.recursive_dynamic.restype = ctypes.c_longlong
libfib_clibO3.recursive_dynamic.argtypes = [ctypes.c_longlong]
libfib_clibO3.iterative.restype = ctypes.c_longlong
libfib_clibO3.iterative.argtypes = [ctypes.c_longlong]
libfib_clibO3.iterative_asm.restype = ctypes.c_longlong
libfib_clibO3.iterative_asm.argtypes = [ctypes.c_longlong]
libfib_clibO3.power_matrix.restype = ctypes.c_longlong
libfib_clibO3.power_matrix.argtypes = [ctypes.c_longlong]


def recursive_dynamic(n):
    return int(libfib_clib.recursive_dynamic(n))

def iterative(n):
    return int(libfib_clib.iterative(n))

def power_matrix(n):
    return int(libfib_clib.power_matrix(n))

def iterative_asm(n):
    return int(libfib_clib.iterative_asm(n))

def recursive_dynamic_O3(n):
    return int(libfib_clibO3.recursive_dynamic(n))

def iterative_O3(n):
    return int(libfib_clibO3.iterative(n))

def iterative_asm_O3(n):
    return int(libfib_clibO3.iterative_asm(n))

def power_matrix_O3(n):
    return int(libfib_clibO3.power_matrix(n))
