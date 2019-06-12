'''
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.


Submission Results:
Runtime: 1780 ms, faster than 5.10% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
Memory Usage: 13.3 MB, less than 50.75% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.

'''


class Solution:
	def longestSubstring(self, s: str, k: int) -> int:
		longest = 0
		for i in range(k, len(s)+1):
			sub = s[:i]
			longest = max(longest, self.check(sub, k))
		return longest
	
	def replaceDelimiters(self, word, k):
		delims = set()
		for key in set(ch for ch in word):
			if word.count(key) < k:
				delims.add(key)
		for d in delims:
			word = word.replace(d, " ")
		return word.split()
	
	def validWords(self, words, k):
		results = list()
		for word in words:
			smaller = self.replaceDelimiters(word, k)
			results.extend(smaller)
		if results != words:
			results = self.validWords(results, k)
		return results
	
	def check(self, s, k):
		words = self.validWords([s], k)
		longest = 0
		for word in words:
			longest = max(longest, len(word))
		return longest