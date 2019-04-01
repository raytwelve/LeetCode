'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        end = len(nums)
        i = 0
        while i < end:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                end -= 1
            else:
                i += 1