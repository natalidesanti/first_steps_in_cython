import time

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n - 1)

n = int(input('Given your number: '))
t1 = time.time()
print("The factorial of this number is", factorial(n))
t2 = time.time()
print("Total time", t2 - t1)
