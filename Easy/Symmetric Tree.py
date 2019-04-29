'''
https://leetcode.com/problems/symmetric-tree/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def isSymmetric(self, root: TreeNode) -> bool:
		if not root: return True
		return self.comp(root.left, root.right)
		
	def comp(self, left, right):
		if (left == None) != (right == None): return False
		if not left and not right: return True

		if left.val == right.val:
			return self.comp(left.left, right.right) and self.comp(left.right, right.left)
		return False