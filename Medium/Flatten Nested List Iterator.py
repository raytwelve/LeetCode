'''
https://leetcode.com/problems/flatten-nested-list-iterator/

Given a nested list of integers, implement an iterator to flatten it.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.
'''



# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
	flatList = None
	index = -1
	last = -1
	def __init__(self, nestedList):
		if nestedList == None: return None
		self.flatList = []
		for nestInt in nestedList:
			self.flatten(nestInt)
		self.index = -1
		self.last = len(self.flatList)-1
		"""
		Initialize your data structure here.
		:type nestedList: List[NestedInteger]
		"""
	def flatten(self, nestInt):
		if nestInt.isInteger():
			self.flatList.append(nestInt.getInteger())
		else:
			nestList = nestInt.getList()
			for intNest in nestList:
				self.flatten(intNest)
		

	def next(self):
		self.index += 1
		return self.flatList[self.index]
		"""
		:rtype: int
		"""
		

	def hasNext(self):
		return self.index < self.last
		"""
		:rtype: bool
		"""
		

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())