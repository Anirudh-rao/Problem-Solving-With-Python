from collections import deque

def SplitAndRoate(arr):
    # String Slicing
    k = 2
    NewArr = arr[k:] + arr[:k]
    print(f"The Existing Array :{arr}")
    print(f" Array Sliciing from new Array:{NewArr}")


arr = [12, 10, 5, 6, 52, 36]
SplitAndRoate(arr)