import time
from total_v5 import computing_total
import numpy as np

t1 = time.time()

n = 10**4
arr = np.arange(n, dtype=np.int)
print("The total is", computing_total(arr))

t2 = time.time()

print('Total time:', t2-t1)
