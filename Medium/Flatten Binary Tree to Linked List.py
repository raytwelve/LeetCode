'''
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

	1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
	3
	 \
	  4
	   \
		5
		 \
		  6


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def flatten(self, root: TreeNode) -> None:
		"""
		Do not return anything, modify root in-place instead.
		"""
		self.swapAndAddLink(root, root)
			
		
	def swapAndAddLink(self, node, lastLink):
		if not node: return lastLink
		
		temp = node.right
		if node.left:
			lastLink.right = node.left
			lastLink = lastLink.right
			lastLink = self.swapAndAddLink(node.left, lastLink)
			node.left = None

		if temp:
			lastLink.right = temp
			lastLink = lastLink.right
			lastLink = self.swapAndAddLink(temp, lastLink)
		return lastLink