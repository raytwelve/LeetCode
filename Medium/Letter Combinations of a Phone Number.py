'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''


class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		digs = [int(x) for x in digits]
		phone = self.buildMap()
		results = list()
		
		if len(digs) > 0:
			self.rec(digs, 0, phone, "", results)
		return results
		
		
	def rec(self, digits, index, phone, string, results):
		if len(string) == len(digits):
			results.append(string)
			return
		
		num = digits[index]
		chars = phone[num]
		
		for x in chars:
			string += x
			self.rec(digits, index+1, phone, string, results)
			string = string[:-1]
		
	def buildMap(self):
		numToChars = dict()
		numToChars[2] = "abc"
		numToChars[3] = "def"
		numToChars[4] = "ghi"
		numToChars[5] = "jkl"
		numToChars[6] = "mno"
		numToChars[7] = "pqrs"
		numToChars[8] = "tuv"
		numToChars[9] = "wxyz"
		return numToChars