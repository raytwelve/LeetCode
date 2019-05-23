''''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
'''

class Solution:
	def searchRange(self, nums: List[int], target: int) -> List[int]:
		# if not nums: return None
		hi = len(nums)-1
		lo = 0
		mid = (lo+hi)//2
		
		while lo <= hi:
			mid = (lo+hi)//2
			if target == nums[mid]:
				left = self.seekLeft(nums, mid)
				right = self.seekRight(nums, mid)
				return [left, right]
			elif target < nums[mid]:
				hi = mid-1
			elif target > nums[mid]:
				lo = mid+1
		return [-1, -1]
	
	
	def seekLeft(self, nums, mid):
		target = nums[mid]
		while mid > -1 and nums[mid] == target:
			mid -= 1
		return mid+1
	def seekRight(self, nums, mid):
		target = nums[mid]
		while mid < len(nums) and nums[mid] == target:
			mid += 1
		return mid-1