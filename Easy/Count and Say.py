'''
https://leetcode.com/problems/count-and-say/

The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.
'''

class Solution:
	def countAndSay(self, n: int) -> str:
		termnum, term = 1, "1"
		while termnum < n:
			termnum += 1
			term = self.countsay(term)
		return term
	
	def countsay(self, s):
		i = 0
		result = ""
		count = 0
		consec = s[i]
		while i < len(s):
			if s[i] == consec:
				count += 1
			else:
				result += str(count) + consec
				count = 1
				consec = s[i]
			i += 1
		result += str(count) + consec
		return result