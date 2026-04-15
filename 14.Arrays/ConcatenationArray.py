"""
You are given an integer array nums of length n.
Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
"""
from ast import List


def getConcatenation(nums:List[int]) -> List[int]:
    ans = []
    ans = nums * 2
    return ans

arr = [22,21,20,1]
res = getConcatenation(arr)

arr = [1,4,1,2]
res = getConcatenation(arr)
