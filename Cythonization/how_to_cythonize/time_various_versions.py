from fib_py import fib_py
from fib_py_cy import fib_py_cy

# In order to be able to import a *.pyx extention file into python
import pyximport
pyximport.install()
from fib_cy import fib_cy

import sys
import timeit

"""
So how do the performance of these different versions compare? 
This script will run 10×100,000 repetitions of each version of our 3 codes, given a Fibonacci 
sequence number (e.g., 30 and later 50) that is supplied as a command line argument:
"""


# pass in Fib number to calculate
n = int(sys.argv[1])

# time each version
t1 = min(timeit.repeat(f"fib_py({n})", number=100000, repeat = 10, setup="from fib_py import fib_py; gc.enable()"))
print(f'Pure python: answer = {fib_py(n)}, time = {t1}, speedup = 1.0')

t = min(timeit.repeat(f"fib_py_cy({n})", number=100000, repeat = 10, setup="from fib_py_cy import fib_py_cy; gc.enable()"))
print(f'Cythonized Python: answer = {fib_py_cy(n)}, time = {t}, speedup = {t1 / t}')

t = min(timeit.repeat(f"fib_cy({n})", number=100000, repeat = 10, setup="from fib_cy import fib_cy; gc.enable()"))
print(f'Typed Cython: answer = {fib_cy(n)}, time = {t}, speedup = {t1 / t}')