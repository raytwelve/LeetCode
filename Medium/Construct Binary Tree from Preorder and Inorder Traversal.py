'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given preorder and inorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
		low = 0
		high = len(preorder)
		rooti = [0]
		
		return self.makeBranch(preorder, rooti, inorder, low, high)
	
	
	def makeBranch(self, preo, rooti, ino, low, high):
		if rooti[0] >= len(preo) or low >= high: return None
		
		rootv = preo[rooti[0]]
		inoi = ino.index(rootv)
		root = TreeNode(rootv)
		
		rooti[0] = 1+ rooti[0]
		root.left = self.makeBranch(preo, rooti, ino, low, inoi)
		root.right = self.makeBranch(preo, rooti, ino, inoi+1, high)
		return root
		