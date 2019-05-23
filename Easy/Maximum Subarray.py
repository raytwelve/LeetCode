'''
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentMax = 0
        maxSumAt = list()
        for i in range(len(nums)):
            currentMax = max(currentMax + nums[i], nums[i])
            maxSumAt.append(currentMax)
        return max(maxSumAt)