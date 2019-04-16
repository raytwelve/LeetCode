'''
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
			  3
		   /	 \
		  9	   20
		/  \	 /  \
	   33  12	15  7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7],
  [33,12,15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution:
	def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
		results = list()
		nodes = list()
		nodes.append(root)
		level_counter = 0
		leftToRight = True
		while len(nodes) > 0:
			level = list()
			while len(nodes) > 0:
				level.append(nodes.pop(0))
			
			flevel = list(filter(None,level))
			
			if len(flevel) > 0:
				results.append([n.val for n in flevel])
				flevel.reverse()
				leftToRight = not leftToRight
				for i in range(len(flevel)):
					n = flevel[i]
					if leftToRight:
						nodes.append(n.left)
						nodes.append(n.right)
					else:
						nodes.append(n.right)
						nodes.append(n.left)
		return results