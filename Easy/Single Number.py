'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		nums.sort()
		lastindex = len(nums)-1
		for i in range(0, lastindex, 2):
			if nums[i] != nums[i+1]:
				return nums[i]
		return nums[lastindex]