'''
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def isBalanced(self, root: TreeNode) -> bool:
		if not root: return True
		if not self.isBalanced(root.left) or not self.isBalanced(root.right): return False
		
		return abs(self.getDepth(root.left) - self.getDepth(root.right)) <=1

	def getDepth(self, node):
		if not node: return 0
		return 1 + max(self.getDepth(node.left), self.getDepth(node.right))