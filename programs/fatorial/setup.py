from distutils.core import setup
from Cython.Build import cythonize

setup(name='Fatorial computation', ext_modules=cythonize("fatorial_program.pyx"))
