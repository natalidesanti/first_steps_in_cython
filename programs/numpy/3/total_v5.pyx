import numpy as np
cimport numpy as np

ctypedef np.int_t DTYPE_t

def computing_total(np.ndarray[DTYPE_t, ndim=1] arr):
    cdef int n
    cdef unsigned long long int total
    cdef int k
    cdef int arr_shape = arr.shape[0]
    total = 0
    for k in range(arr_shape):
       total += arr[k]
    return total
