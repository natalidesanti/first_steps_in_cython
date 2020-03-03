import numpy as np
cimport numpy as np

ctypedef np.int_t DTYPE_t
def computing_total(np.ndarray[DTYPE_t, ndim=1] arr):
    cdef int n
    cdef unsigned long long int total
    cdef int k
    total = 0
    for k in arr:
       total += k
    return total