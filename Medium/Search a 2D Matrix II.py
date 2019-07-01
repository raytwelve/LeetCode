'''
https://leetcode.com/problems/search-a-2d-matrix-ii/

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example:
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.
Given target = 20, return false.

'''

class Solution:
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		if not matrix: return False
		# high = len(matrix[0])-1
		
		for row in matrix:
			found = self.binSearch(row, target)
			if found: return True
		return False
	
	def binSearch(self, nums, target):
		low = 0
		high = len(nums)-1
		while low <= high:
			mid = (low + high) //2
			if target == nums[mid]: return True
			elif target < nums[mid]:
				high = mid-1
			else:
				low = mid + 1
		return False