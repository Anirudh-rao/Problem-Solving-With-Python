import enum
from functools import reduce

def SumOfArray(arr):
    ans = sum(arr)
    print(f"The Sum of Array {arr} is {ans}")
    ans = reduce(lambda a,b:a+b, arr)
    print(f"The Sum of Array {arr} is {ans} using functtools")
    t = 0
    for x in arr:
        t += x
    print(f"The Sum of Array {arr} is {ans} using iterations")
    t = 0
    for i,val in enumerate(arr):
        t += val
    print(f"The Sum of Array {arr} is {ans} using enumerate")
    
arr = [12, 3, 4, 15]
SumOfArray(arr)