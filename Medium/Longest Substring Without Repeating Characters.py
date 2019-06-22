'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.
'''


class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		if not s: return 0
		longest = 0
		leng = 0
		used = list()
		for i in range(len(s)):
			ch = s[i]
			if ch not in used:
				used.append(ch)
				leng += 1
			else:
				used = used[used.index(ch)+1:]
				used.append(ch)
				newlen = len(used)
				longest = max(longest, leng, newlen)
				leng = newlen
		return max(longest, leng)