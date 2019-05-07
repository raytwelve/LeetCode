'''
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
		# use median item as root
		# use median item of left sublist as leftchild
		# use median item of right sublist as rightchild
		# continue until lo == hi
		lo = 0
		hi = len(nums)-1
		
		if hi < 0: return None
		return self.assignMid(nums, lo, hi)
		
		
	def assignMid(self, nums, lo, hi):
		mid = (hi-lo)//2 + lo
		node = TreeNode(nums[mid])
		
		if mid > lo:
			node.left = self.assignMid(nums, lo, mid-1)
		if hi > mid:
			node.right = self.assignMid(nums, mid+1, hi)
		return node