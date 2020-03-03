import time
from integration_cython import integrate_f

a = 0
b = 1000
N = 10000

t1 = time.process_time()

print(integrate_f(a, b, N))

t2 = time.process_time()

print('Total time:', t2-t1)
