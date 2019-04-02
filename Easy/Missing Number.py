'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        full_range = set(range(len(nums)+1))
        for n in nums:
            full_range.discard(n)
        return full_range.pop()