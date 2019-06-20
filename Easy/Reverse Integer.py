'''
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution:
	def reverse(self, x: int) -> int:
		isNeg = x < 0
		rev = int(str(abs(x))[::-1])
		if isNeg:
			return 0 if rev > 2**31 else -rev
		else:
			return 0 if rev >= 2**31 else rev