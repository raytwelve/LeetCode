# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution:
	def inorderTraversal(self, root: TreeNode) -> List[int]:
		# a
		# results = list()
		# self.recursiveInPlace(root, results)
		# b
		# results = self.recursiveReturn(root)
		# c
		results = self.iterative(root)
		
		return results
	
	def recursiveInPlace(self, node, results):
		if node == None:
			return
		self.recursiveInPlace(node.left, results)
		results.append(node.val)
		self.recursiveInPlace(node.right, results)
	
	def recursiveReturn(self, node):
		if node == None:
			return []
		return self.recursiveReturn(node.left) + [node.val] + self.recursiveReturn(node.right)
		
	def iterative(self, node):
		if node == None:
			return []
		results = list()
		breadcrumbs = list()
		visited = set()
		breadcrumbs.append(node)
		while len(breadcrumbs) > 0:
			walker = breadcrumbs[-1]
			if walker.left != None and walker.left not in visited:
				breadcrumbs.append(walker.left)
				continue
			walker = breadcrumbs.pop()
			visited.add(walker)
			results.append(walker.val)
			
			if walker.right != None:
				breadcrumbs.append(walker.right)
				# continue
		return results