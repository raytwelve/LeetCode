'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/789/

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
Note:
You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
'''


"""
# Definition for a Node.
class Node:
	def __init__(self, val, left, right, next):
		self.val = val
		self.left = left
		self.right = right
		self.next = next
"""
class Solution:
	def connect(self, root: 'Node') -> 'Node':
		results = list()
		nodes = list()
		nodes.append(root)
		while len(nodes) > 0:
			level = list()
			while len(nodes) > 0:
				level.append(nodes.pop(0))
			
			flevel = list(filter(None,level))
			if len(flevel) > 0:
				results.append(list(map(lambda n: n.val, flevel)))
				for i in range(len(flevel)-1):
					flevel[i].next = flevel[i+1]
					nodes.append(flevel[i].left)
					nodes.append(flevel[i].right)
				flevel[-1].next = None
				nodes.append(flevel[-1].left)
				nodes.append(flevel[-1].right)
		return root