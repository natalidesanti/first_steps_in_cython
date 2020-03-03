import time
from total_v3 import computing_total

t1 = time.time()

n = 10**4
print("The total is", computing_total(n))

t2 = time.time()

print('Total time:', t2-t1)
