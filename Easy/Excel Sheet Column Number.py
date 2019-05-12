'''
https://leetcode.com/problems/excel-sheet-column-number/

Given a column title as appear in an Excel sheet, return its corresponding column number.
'''

class Solution:
	def titleToNumber(self, s: str) -> int:
		sum = 0
		for i in range(len(s)):
			# in python, we can iterate with negative indices, which starts with the last item as -1, second to last as -2 ... etc
			
			# therefore, -1 == len(s)-1
			
			# using this info, we can manipulate our range of i = [0, len(s)-1] --> [-1, -len(s)]
			ch = s[-(i+1)]
			sum += (ord(ch) - ord('A') + 1) * 26**i
		return sum