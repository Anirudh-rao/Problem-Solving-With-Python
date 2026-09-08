from functools import reduce

def LargestArray(arr):
    print(f"Max value of array",max(arr))
    res = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > res:
            res = arr[i]
    print(f"From standard function",res)
    reduceFunction = reduce(max, arr)
    print(f"From functools function",reduceFunction)
    arr.sort()
    result = arr[-1]
    print(f"From sorted  function",result)


arr = [10, 324, 45, 90, 9808]
LargestArray(arr)




