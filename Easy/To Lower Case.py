'''
https://leetcode.com/problems/to-lower-case/

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
'''


class Solution:
	def toLowerCase(self, str: str) -> str:
		# return str.lower()
		result = ""
		for s in str:
			asc = ord(s)
			if asc >= 65 and asc <= 90:
				asc += 32
			result += chr(asc)
		return result