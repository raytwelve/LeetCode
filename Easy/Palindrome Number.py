'''
https://leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
Follow up:
Coud you solve it without converting the integer to a string?
'''

class Solution:
	def isPalindrome(self, x: int) -> bool:
		if x == 0: return True
		if x < 0 or x % 10 == 0: return False
		
		digits = list()
		while x > 0:
			digits.append(x % 10)
			x = x//10
		
		for i in range(len(digits)//2+1):
			if digits[i] != digits[-1-i]: return False
		return True