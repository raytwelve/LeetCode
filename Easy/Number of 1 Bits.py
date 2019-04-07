'''
https://leetcode.com/problems/number-of-1-bits/

Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

Note:
Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.

Follow up:
If this function is called many times, how would you optimize it?
'''
import sys

class Solution(object):
	def solution1(self, n):
		return bin(n).count('1')
	def solution2(self, n):
	# note: in python, int are objects as well, thus has overhead data;
	# also will increase in size to accomodate larger numbers--kind of like an arraylist; it is not a fixed size, as in C
	bits = sys.getsizeof(n) * 8
	ones = 0
	for i in range(bits):
		ones += n>>i & 1
	return ones
	def hammingWeight(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		return self.solution1(n)