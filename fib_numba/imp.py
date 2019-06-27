import numpy as np
import numba

@numba.jit(numba.int64(numba.int64,numba.int64[:]),nopython=True)
def recursive_dynamic_imp(n, val_array):
    if val_array[n] != -1:
        return val_array[n]
    else:
        val_array[n] = recursive_dynamic_imp(n-1,val_array)+\
                       recursive_dynamic_imp(n-2,val_array)
        return val_array[n]

@numba.jit(numba.int64(numba.int64),nopython=True)
def recursive_dynamic(n):
    val_array = np.full(n+1,-1, dtype=np.int64)
    val_array[0] = 0
    val_array[1] = 1
    return recursive_dynamic_imp(n, val_array)

@numba.jit(numba.int64(numba.int64),nopython=True)
def iterative(n):
    if n < 2:
        return n
    # initial values
    fh = np.int64(1)
    fl = np.int64(0)
    for i in range(2,n+1):
        # Save in temp location
        temp = fh
        # get new high value
        fh = fh+fl
        # save old value in low value
        fl = temp
    return fh

@numba.jit(numba.int64[:,:](numba.int64[:,:],numba.int64[:,:]),nopython=True)
def matmul(A,B):
    C = np.array([[0,0],[0,0]],dtype=np.int64)
    C[0,0] = A[0,0]*B[0,0]+A[0,1]*B[1,0]
    C[0,1] = A[0,0]*B[0,1]+A[0,1]*B[1,1]
    C[1,0] = A[1,0]*B[0,0]+A[1,1]*B[1,0]
    C[1,1] = A[1,0]*B[0,1]+A[1,1]*B[1,1]
    return C

@numba.jit(numba.int64[:](numba.int64[:,:],numba.int64[:]),nopython=True)
def matvecmul(A,v):
    C = np.array([0,0],dtype=np.int64)
    C[0] = A[0,0]*v[0]+A[0,1]*v[1]
    C[1] = A[1,0]*v[0]+A[1,1]*v[1]
    return C

@numba.jit(numba.int64[:,:](numba.int64[:,:],numba.int64),nopython=True)
def build_power_matrix(A, n):
    if n == 1:
        return A
    if n%2 == 0:
        Anew = build_power_matrix(A,n//2)
        return matmul(Anew,Anew)
    else:
        Aev = build_power_matrix(A,n//2)
        return matmul(Aev,matmul(Aev,A))

@numba.jit(numba.int64(numba.int64),nopython=True)
def power_matrix(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    init_vec = np.array([1,1], dtype=np.int64)
    A = np.array([[1,1],[1,0]], dtype=np.int64)
    A_power = build_power_matrix(A,n-2)
    return matvecmul(A_power,init_vec)[0]
