import time

def f(x):
    return 1 + x + x**2

def integrate_f(a, b, N):
    s = 0
    dx = (b - a)/N
    for i in range(N):
        s += f(a + i*dx)
    return s*dx

t1 = time.process_time()

a = 0
b = 1000
N = 10000

print(integrate_f(a, b, N))

t2 = time.process_time()

print('Total time:', t2-t1)
