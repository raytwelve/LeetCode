'''
https://leetcode.com/problems/convert-bst-to-greater-tree/

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def convertBST(self, root: TreeNode) -> TreeNode:
		self.revorder(root, [0])
		return root
		
		
	def revorder(self, node, total):
		if not node: return None
		self.revorder(node.right, total)
		node.val += total[0]
		total[0] = node.val
		
		self.revorder(node.left, total)