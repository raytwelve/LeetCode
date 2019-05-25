'''
https://leetcode.com/problems/invert-binary-tree/

Invert a binary tree.

Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def invertTree(self, root: TreeNode) -> TreeNode:
		if not root: return None
		self.childSwap(root)
		return root
		
		
	def childSwap(self, node):
		node.left, node.right = node.right, node.left
		if node.left: self.childSwap(node.left)
		if node.right: self.childSwap(node.right)