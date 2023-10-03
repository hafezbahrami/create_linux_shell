# cython: profile=True

### Function for finding n'th Fibonacci number. Copied from (Kurt W. Smith, "Cython", O'Reilly Media Inc., 2015).
### Typed Cython version

### The third version, fib_cy.pyx, is a Cythonic implementation. Note the new file ending, .pyx, for Cython source 
### files. Each variable is now statically typed as an integer. In the function body, this is done by prefacing the 
### variable definition by cdef. The cdef is not necessary for arguments in the function definition (e.g., n).



def fib_cy(int n):
    cdef int a = 0
    cdef int b = 1
    cdef int i
    for i in range(n - 1):
        a, b = a + b, a
    return a