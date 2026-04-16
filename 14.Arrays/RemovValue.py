
"""
Given an integer array nums and an integer val,
remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
"""


import array
from typing import List


def removeElement(nums: List[int], val: int) -> int:
        i = 0
        arr = []
        for j in range (len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i+= 1
        return i


arr = [3,2,2,3]
print(removeElement(arr, 3))