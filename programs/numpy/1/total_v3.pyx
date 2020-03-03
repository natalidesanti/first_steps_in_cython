import numpy as np
cimport numpy as np

def computing_total(int n):
    cdef unsigned long long int total
    cdef int k
    cdef np.ndarray[np.int_t, ndim=1] arr
    total = 0
    arr = np.arange(n, dtype=np.int)
    for k in arr:
       total += k
    return total