import fib
import timeit
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", help="Fibonacci number to compute", type=int)
parser.add_argument("-N", help="The number of times the test is executed", type=int)

args = parser.parse_args()

if args.n is not None:
    fib_num = args.n
else:
    fib_num = 92

if args.N is not None:
    num_executions = args.N
else:
    num_executions = 100000

# The 92nd fibonacci number: 6343304842483959687 fits within an int64.

print("The {}th fibonachi number is: {}".format(fib_num, fib.fib_iterative_basic_python(fib_num)))

print(timeit.timeit('fib.fib_recursive_dynamic_basic_python({})'.format(fib_num), setup='import fib', number=100000))
print(timeit.timeit('fib.fib_iterative_basic_python({})'.format(fib_num), setup='import fib', number=100000))
