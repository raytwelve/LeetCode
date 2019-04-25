'''
https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.

Note:
You must return the copy of the given head as a reference to the cloned list.
'''

"""
# Definition for a Node.
class Node:
	def __init__(self, val, next, random):
		self.val = val
		self.next = next
		self.random = random
"""

"""
# Definition for a Node.
class Node:
	def __init__(self, val, next, random):
		self.val = val
		self.next = next
		self.random = random
"""
class Solution:
	def copyRandomList(self, head: 'Node') -> 'Node':
		print(type(head))
		oglist = self.listify(head)
		randomIndexMap = self.createMap(oglist)
		nulist = self.createNewList(oglist)
		
#         link next and randoms
		self.linkNodes(nulist, randomIndexMap)
		nuhead = nulist[0]
		return nuhead
		
	def listify(self, node):
		lis = list()
		while node:
			lis.append(node)
			node = node.next
		return lis
		
	def createMap(self, oglist):
		randomIndexMapping = list()
		for node in oglist:
			if not node.random:
				randomIndexMapping.append(-1) #will append None to end of this list; -1 is index for last item in list
			else:
				randex = oglist.index(node.random)
				randomIndexMapping.append(randex)
				
		randomIndexMapping.append(None)
		return randomIndexMapping
		
	def createNewList(self,oglist):
		cpy = list()
		for node in oglist:
			cpy.append(self.createNode(node))
		cpy.append(None)
		return cpy
		
	def createNode(self, aNode):
		bNode = Node(None,None,None)
		bNode.val = aNode.val
		return bNode

	def linkNodes(self, nodes, indices):
		for i in range(len(nodes)-1):
			nodes[i].next = nodes[i+1]
			
			rndm = indices[i]
			nodes[i].random = nodes[rndm]