from functools import reduce


def RemainderOfArray(arr,n):
    result = 1
    l = len(arr)
    for i in range(1, len(arr)):
        result *= arr[i]
    remainder = result % n
    return remainder


arr = [100, 10, 5, 25, 35, 14]
n = 11
print(f"Remainder from generarl approach {RemainderOfArray(arr, n)}")
rem1 = reduce(lambda x,y:(x*y) %n , arr)
print(f"Using the Reduce function:{rem1}")