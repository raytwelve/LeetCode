'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = list()
        sz = len(nums)-1
        for i in range(sz):
            num = nums[i]
            com = target - num
            if nums[i+1:].count(com) > 0:
                ans.append(i)
                ans.append(nums.index(com, i+1))
                return ans