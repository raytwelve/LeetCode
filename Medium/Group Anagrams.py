'''
https://leetcode.com/problems/group-anagrams/

Given an array of strings, group anagrams together.
Note:
All inputs will be in lowercase.
The order of your output does not matter.
'''

class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		anagrams = dict()
		for s in strs:
			ssorted = str(sorted(s))
			if ssorted in anagrams.keys():
				anagrams[ssorted].append(s)
			else:
				anagrams[ssorted] = [s]
		return list(anagrams.values())