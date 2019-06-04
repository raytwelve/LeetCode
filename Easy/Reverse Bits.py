'''
https://leetcode.com/problems/reverse-bits/

Reverse bits of a given 32 bits unsigned integer.
Note:
Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 
Follow up:
If this function is called many times, how would you optimize it?

'''

class Solution:
	# @param n, an integer
	# @return an integer
	def reverseBits(self, n):
		bits = 32
		binary = bin(n)[2:]
		reverse = binary[::-1]
		zeropads = '0' * (bits - len(binary))
		return int(reverse + zeropads, 2) 