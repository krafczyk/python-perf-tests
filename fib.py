def fib_recursive_dynamic_basic_python_imp(n, dictionary):
    if n < 2:
        return n
    elif n in dictionary:
        return dictionary[n]
    else:
        dictionary[n] = fib_recursive_dynamic_basic_python_imp(n-1,dictionary)+\
                        fib_recursive_dynamic_basic_python_imp(n-2,dictionary)
        return dictionary[n]

def fib_recursive_dynamic_basic_python(n):
    new_dict = {}
    return fib_recursive_dynamic_basic_python_imp(n, new_dict)

def fib_iterative_basic_python(n):
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
