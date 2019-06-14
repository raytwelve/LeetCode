'''
https://leetcode.com/problems/merge-two-binary-trees/

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Note: The merging process must start from the root nodes of both trees.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
		if not t1 and not t2: return None
		
		v1 = 0 if not t1 else t1.val
		v2 = 0 if not t2 else t2.val
		
		head = TreeNode(v1+v2)
		
		self.mergeNodes(t1, t2, head)
		return head
	
	def mergeNodes(self, node1, node2, node3):
		left1 = None if not node1 else node1.left
		left2 = None if not node2 else node2.left
		right1 = None if not node1 else node1.right
		right2 = None if not node2 else node2.right
		
		lv1 = 0 if not left1 else left1.val
		lv2 = 0 if not left2 else left2.val
		rv1 = 0 if not right1 else right1.val
		rv2 = 0 if not right2 else right2.val
		
		if left1 or left2:
			node3.left = TreeNode(lv1+lv2)
			self.mergeNodes(left1, left2, node3.left)
		if right1 or right2:
			node3.right = TreeNode(rv1 + rv2)
			self.mergeNodes(right1, right2, node3.right)