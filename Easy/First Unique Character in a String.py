'''
https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
'''

class Solution:
	def firstUniqChar(self, s: str) -> int:
		if not s: return -1
		
		charcount = dict()
		for c in set(s):
			n = s.count(c)
			charcount[c] = n
		for i in range(len(s)):
			if charcount[s[i]] == 1: return i
		return -1