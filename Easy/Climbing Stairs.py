'''
https://leetcode.com/problems/climbing-stairs/

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
'''



class Solution:
	def climbStairs(self, n: int) -> int:
		twoSteps = n //2
		ways = 0
		
		for kay in range(0, twoSteps+1):
			en = n-(kay*2) + kay
			# en choose kay
			numerator = self.factorial(en)
			denominator = self.factorial(kay)*self.factorial(en-kay)
			ways += (numerator//denominator)
		return ways
	
	
	def factorial(self, num):
		result = 1
		for i in range(1, num+1):
			result *= i
		return result