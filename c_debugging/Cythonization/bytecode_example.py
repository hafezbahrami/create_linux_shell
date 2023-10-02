# Reference: https://stackoverflow.com/questions/3299648/python-compilation-interpretation-process
#            https://www.youtube.com/watch?v=PJ16cdc0YKM&ab_channel=IDGTECHtalk

def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)

res = fib(10)
print(res)

"""
importing dis, as diassmble bytecode package.
We will see that bytecode is a little different than assembly code, that is usually derived from
compiling languages such as C, C++, Java, ...
"""

import dis
dis.dis(fib)

aaa = -1