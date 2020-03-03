from distutils.core import setup
from Cython.Build import cythonize

setup(name='Computing total', ext_modules=cythonize("total_v3.pyx"))
