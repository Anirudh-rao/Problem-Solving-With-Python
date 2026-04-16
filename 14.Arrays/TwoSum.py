"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
"""


from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in arr:
                return [arr[complement],i]
            arr[num] = i

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))