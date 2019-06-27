import fib_basic
import timeit
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", help="Fibonacci number to compute", type=int)
parser.add_argument("-N", help="The number of times the test is executed", type=int)
parser.add_argument("--short", help="Only compute values for testing, no long timed test", action='store_true')

args = parser.parse_args()

if args.n is not None:
    fib_num = args.n
else:
    fib_num = 92

if args.N is not None:
    num_executions = args.N
else:
    num_executions = 100000

short = args.short

# The 92nd fibonacci number: 6343304842483959687 fits within an int64.

print("The {}th fibonachi number is: {}".format(fib_num, fib_basic.iterative(fib_num)))

print(fib_basic.recursive_dynamic(fib_num))
print(fib_basic.iterative(fib_num))
print(fib_basic.power_matrix(fib_num))

if not short:
    print(timeit.timeit('fib_basic.recursive_dynamic({})'.format(fib_num), setup='import fib_basic', number=100000))
    print(timeit.timeit('fib_basic.iterative({})'.format(fib_num), setup='import fib_basic', number=100000))
    print(timeit.timeit('fib_basic.power_matrix({})'.format(fib_num), setup='import fib_basic', number=100000))
