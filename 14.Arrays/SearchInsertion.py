"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
"""

from ast import List


def searchInsert(self, nums: List[int], target: int) -> int:
        le = len(nums)
        for i in range(le):
            if nums[i] >= target:
                return i
            
            
        return le


arr = [1,3,5,6]
target = 5
print(searchInsert(arr, target))  # Output: 2