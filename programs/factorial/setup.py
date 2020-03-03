from distutils.core import setup
from Cython.Build import cythonize

setup(name='Factorial computation', ext_modules=cythonize("factorial_program.pyx"))
