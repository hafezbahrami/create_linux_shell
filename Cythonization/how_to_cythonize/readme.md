# Various References for Cythonization
[main reference](https://waterprogramming.wordpress.com/2022/06/29/cythonizing-your-python-code-part-1-the-basics/)


## 1 various files in this project
files fib_py.py [pure python code] and fib_py_cy.py [Cythonized python code] are identical, we only use the latter one for Cythonization in the setup.py file. fib_cy.pyx [Typed Cython code] is basically the same file writtten in Pyrex programming language ([read hear](https://www.openmyfiles.com/pyx-file/)).

The above 3 files are repeated to int declared variables in *.pyx to double type.

_A little more on Cythonic implementation:_ The third version of files, for instance "fib_cy.pyx", is a **Cythonic implementation**. Note the new file ending, *.pyx, for Cython source files. Each variable is now statically typed as an integer. In the function body, this is done by prefacing the variable definition by cdef. The cdef is not necessary for arguments in the function definition (e.g., n).
```
def fib_cy(int n):
    cdef int a = 0
    cdef int b = 1
    cdef int i
    for i in range(n - 1):
        a, b = a + b, a
    return a
```

## 2 calculate the speedup in Fibonacci number
If we run as below, we can see the Typed Cython code, where we statically type all the variables, will speed up significantly. This just simply shows that 
dynamically typed variables in any Python code is the main reason for slowing down the python code:
```
python3 time_various_versions.py 30
```

If we repeate the above command, but this time passing 50 to calculate Fibonacci number, the Typed python version gives a wrong answer, as the statically allocated 
memory for an int can not contain the largness of the result. For this, we need to run the "double" version of the 3 files and allocate more memmory for the results.




## 2 how to create a .c file from a py file
We can use Cython package for create a *.c file out of *.py file. Then using the GCC package to create an executable for this *.c file, like we do in other 
low level langiages. This *.exe file can be executed as usual.

[Reference](https://stackoverflow.com/questions/5105482/compile-main-python-program-using-cython)
