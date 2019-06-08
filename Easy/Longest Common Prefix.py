'''
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Note:
All given inputs are in lowercase letters a-z.
'''



class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		if not strs: return ""
		prefix = ""
		shortest = min(len(x) for x in strs)
		for i in range(shortest):
			ch = set(x[i] for x in strs)
			if len(ch) != 1:
				break
			prefix += ch.pop()
		return prefix