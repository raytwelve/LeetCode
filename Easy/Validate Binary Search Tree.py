'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/
'''

# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution:
	def isValidBST(self, root: TreeNode) -> bool:
		if root == None:
			return True
		
		return (root.left == None or root.val >= root.left.val) and (root.right == None or root.val <= root.right.val) and self.isValidBST(root.left) and self.isValidBST(root.right)
		