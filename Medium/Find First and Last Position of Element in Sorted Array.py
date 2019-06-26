'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
'''


class Solution:
	def searchRange(self, nums: List[int], target: int) -> List[int]:
		low = 0
		high = len(nums)-1
		
		return self.find(nums, low, high, target)
		
	def find(self, nums, low, high, target):
		if low > high: return [-1, -1]
		mid = (low + high)//2
		if target == nums[mid]:
			start = self.getBound(nums, target, mid, low-1, -1)
			end = self.getBound(nums, target, mid, high+1, 1)
			return [start, end]
		elif target > nums[mid]:
			return self.find(nums, mid+1, high, target)
		elif target < nums[mid]:
			return self.find(nums, low, mid-1, target)
			
			
	def getBound(self, nums, target, start, end, inc):
		last = -1
		for i in range(start, end, inc):
			if target != nums[i]: break
			last = i
		return last