'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

Given an array, rotate the array to the right by k steps, where k is non-negative.
Note:
- Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
- Could you do it in-place with O(1) extra space?
'''

class Solution:
	def rotate(self, nums: List[int], k: int) -> None:
		if k % len(nums) == 0:
			return
		
		br = len(nums)-k % len(nums)
		
		st = nums[br:]
		en = nums[:br]
		nums.clear()
		nums.extend(st)
		nums.extend(en)