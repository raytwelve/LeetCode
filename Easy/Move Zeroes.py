'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution:
	def solution2(self, nums: List[int]) -> None:
		size = len(nums)
		nonzero = list(filter(lambda x: x != 0, nums))
		zeroes = size - len(nonzero)
		nonzero.extend([0]*zeroes)

		nums.clear()
		nums.extend(nonzero)

	def solution1(self, nums: List[int]) -> None:
		end = len(nums)
		i = 0
		while i < end:
			if nums[i] == 0:
				nums.append(nums.pop(i))
				end -= 1
			else:
				i += 1

	def moveZeroes(self, nums: List[int]) -> None:
		self.solution1(nums)
		self.solution2(nums)