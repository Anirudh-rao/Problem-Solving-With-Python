import math
import numpy as np


def factorial(n,f):
    print(f"The Factorial of number {n} is :",math.factorial(n))
    print(f"Second method to find factorial of {n} is",np.prod(range(1,n+1)))
    for i in range(1, n+1):
        f *= i
    print(f"Third method to find factorial of {n} is",f)


factorial(6,1)
factorial(6,5)
