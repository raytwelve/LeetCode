'''
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.
'''

class Solution:
	def findAnagrams(self, s: str, p: str) -> List[int]:
		indices = list()
		pCount = self.makeDict(p)
		sCount = self.makeDict(s[:len(p)])
		if self.compareDicts(pCount, sCount): indices.append(0)
		
		for i in range(len(p), len(s)):
			add = s[i]
			remove = s[i-len(p)]
			self.updateDict(add, remove, sCount)
			if self.compareDicts(pCount, sCount): indices.append(i-len(p)+1)
		return indices
	
	def makeDict(self, s):
		count = dict()
		for ch in s:
			if ch in count.keys(): count[ch] += 1
			else: count[ch] = 1
		return count
	
	def updateDict(self, add, remove, count):
		if add in count.keys(): count[add] += 1
		else: count[add] = 1
		count[remove] -= 1
			
	def compareDicts(self, p, s):
		for k,v in p.items():
			if k not in s.keys(): return False
			if s[k] != v: return False
		return True