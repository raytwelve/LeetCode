'''
https://leetcode.com/problems/search-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

'''


class Solution:
	def search(self, nums: List[int], target: int) -> int:
#		 solution1:	shift array back to retular sorted
#					   run binary serach
#		 solution2:	find point where array 'overflows'
#					   use that index as offset to mid to do modulus math
#					   run binary search, while accounting for modulus
		# O(n + log n)
		offset = 0
		for i in range(len(nums)-1):
			if nums[i] > nums[i+1]:
				offset = i+1
				break
		
		size = len(nums)
		high = len(nums)-1
		low = 0
		mid = None
		
		
		while low <= high:
			mid = (high-low)//2 + low
			if target == nums[(mid+offset)%size]:
				return (mid+offset) % size
			if target > nums[(mid+offset) % size]:
				low = mid+1
			else:
				high = mid-1
		return -1