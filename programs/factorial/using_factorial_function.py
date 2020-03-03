from factorial_program import factorial
import time

n = int(input('Given your number: '))
t1 = time.time()
print("The factorial of this number is", factorial(n))
t2 = time.time()
print("Total time", t2 - t1)
