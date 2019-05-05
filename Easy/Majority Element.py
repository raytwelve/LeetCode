'''
https://leetcode.com/problems/majority-element/

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for x in set(nums):
            count = nums.count(x)
            if count > len(nums)//2: return x