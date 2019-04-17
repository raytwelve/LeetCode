'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Note:
All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution:
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		lca = None
		pRoute = list()
		qRoute = list()
		
		if not self.findRoute(root, p, pRoute) or not self.findRoute(root, q, qRoute):
			return None
		
		for i in range(min(len(pRoute), len(qRoute))):
			if pRoute[i] != qRoute[i]: break
			lca = pRoute[i]
		return lca
		
	def findRoute(self, traveler, target, route):
		if traveler == target:
			route.insert(0, traveler)
			return True
		
		if traveler.left:
			if self.findRoute(traveler.left, target, route):
				route.insert(0, traveler)
				return True
		if traveler.right: 
			if self.findRoute(traveler.right, target, route):
				route.insert(0, traveler)
				return True
		return False