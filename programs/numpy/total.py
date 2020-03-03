import time
t1 = time.time()

import numpy as np

def computing_total(n):
    total = 0
    arr = np.arange(n)
    for k in arr:
        total = total + k
    return total

n = 10**4

print(computing_total(n))

t2 = time.time()
t = t2 - t1
print('Total time: ', t)
