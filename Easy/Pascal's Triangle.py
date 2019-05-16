'''
https://leetcode.com/problems/pascals-triangle/

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
'''
class Solution(object):
	def generate(self, numRows):        
		if numRows == 0: return []
		
		row = [1]
		results = []
		results.append(row.copy())
		for i in range(1, numRows):
			prev = 0
			for j in range(len(row)):
				curr = row[j]
				row[j] = prev + curr
				prev = curr
			row.append(1)
			results.append(row.copy())
		return results