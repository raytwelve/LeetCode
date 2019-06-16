'''
https://leetcode.com/problems/factorial-trailing-zeroes/

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''


class Solution:
	def trailingZeroes(self, n: int) -> int:
		zeros = 0
		n = n//5
		while n != 0:
			zeros += n
			n = n//5
		return zeros