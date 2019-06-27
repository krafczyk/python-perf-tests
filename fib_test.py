import fib_basic
import fib_cython
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

mods = { 'fib_basic': fib_basic, 'fib_cython': fib_cython}

print("\nVerification of values:")
for mod_name in mods:
    print("module {}".format(mod_name))
    for alg_name in mods[mod_name].algos:
        print("{}: {}".format(alg_name, mods[mod_name].algos[alg_name](fib_num)))

print("\nBegin testing performance")
if not short:
    for mod_name in mods:
        for alg_name in mods[mod_name].algos:
            result = timeit.timeit('{}.{}({})'.format(mod_name,alg_name,fib_num),
                                   setup='import {}'.format(mod_name),
                                   number=num_executions)
            print("{} {}: {}".format(mod_name, alg_name, result))
