def recursive_dynamic_imp(n, dictionary):
    if n < 2:
        return n
    elif n in dictionary:
        return dictionary[n]
    else:
        dictionary[n] = fib_recursive_dynamic_basic_python_imp(n-1,dictionary)+\
                        fib_recursive_dynamic_basic_python_imp(n-2,dictionary)
        return dictionary[n]

def recursive_dynamic(n):
    new_dict = {}
    return recursive_dynamic_imp(n, new_dict)

def iterative(n):
    if n < 2:
        return n
    # initial values
    fh = 1
    fl = 0
    for i in range(2,n+1):
        # Save in temp location
        temp = fh
        # get new high value
        fh = fh+fl
        # save old value in low value
        fl = temp
    return fh

def mat_mult(A, B):
    C = [[0,0],[0,0]]
    C[0][0] = A[0][0]*B[0][0]+A[0][1]*B[1][0]
    C[0][1] = A[0][0]*B[0][1]+A[0][1]*B[1][1]
    C[1][0] = A[1][0]*B[0][0]+A[1][1]*B[1][0]
    C[1][1] = A[1][0]*B[0][1]+A[1][1]*B[1][1]
    return C

def mat_mult_v(A, v):
    res = [[0],[0]]
    res[0][0] = A[0][0]*v[0][0]+A[0][1]*v[1][0]
    res[1][0] = A[1][0]*v[0][0]+A[1][1]*v[1][0]
    return res

def build_power_matrix(A, n):
    if n == 1:
        return A
    if n%2 == 0:
        Anew = build_power_matrix(A,(int)(n/2))
        return mat_mult(Anew,Anew)
    else:
        Aev = build_power_matrix(A,(int)(n/2))
        Aodd = mat_mult(Aev,A)
        return mat_mult(Aev,Aodd)

def power_matrix(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    init_vec = [[1],[1]]
    A = [[1,1],[1,0]]
    A_power = build_power_matrix(A,n-2)
    return mat_mult_v(A_power,init_vec)[0][0]
