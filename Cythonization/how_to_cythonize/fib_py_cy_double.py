### Function for finding n'th Fibonacci number. Copied from (Kurt W. Smith, "Cython", O'Reilly Media Inc., 2015).
### Pure Python version that we will cythonize

# This file, fib_py_cy_double.py, is identical to the fib_py_doubl.py script. We will “Cythonize” it to 
# compiled C code without making any manual changes.

def fib_py_cy_double(n):
    a, b = 0., 1.
    for i in range(n - 1):
        a, b = a + b, a
    return a