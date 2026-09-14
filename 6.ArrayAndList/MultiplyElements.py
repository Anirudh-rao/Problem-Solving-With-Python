import math
from functools import reduce
from operator import mul

def MultiplyElements(a):
    print(f"The Original List :{a}")
    res = math.prod(a)
    print(f"The Product of elements:{res}")
    res = 1
    for i in a:
        res *= i
    print(f"The Product of elements using for loop:{res}")
    res = 0
    res = reduce(mul,a)
    print(f"The Product of elements using reduce:{res}")

a = [2, 4, 8, 3]
MultiplyElements(a)