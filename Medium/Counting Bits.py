'''
https://leetcode.com/problems/counting-bits/

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Follow up:
It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''


class Solution:
	def countBits(self, num: int) -> List[int]:
		onecounts = dict()
		onecounts[0] = 0
		
		
		for i in range(1,num+1):
			onebits = 0
			expo = int(math.log(i,2))
			rem = i-2**expo
			onecounts[i] = 1+onecounts[rem]
		return list(onecounts.values())