'''
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''


class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		# its imporant to check needle before haystack
		# not will return true if object either null or empty
		# test case: "" == "" should return 0
		if not needle: return 0
		if not haystack: return -1
		
		
		for i in range(len(haystack)-len(needle)+1):
			hay = haystack[i:i+len(needle)]
			if hay == needle: return i
		return -1
	
	# def checkMatch(self, a, b):
	#     return a == b