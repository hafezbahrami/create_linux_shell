# Reference: https://waterprogramming.wordpress.com/2022/06/29/cythonizing-your-python-code-part-1-the-basics/

from setuptools import setup
from Cython.Build import cythonize

list_of_files_to_cythonize = ['fib_py_cy.py', 'fib_cy.pyx'] # ['fib_py_cy.py', 'fib_cy.pyx', 'fib_py_cy_double.py', 'fib_cy_double.pyx']
cythonized_obj = cythonize(list_of_files_to_cythonize, annotate=True, language_level=3)
                                

setup(ext_modules = cythonized_obj)