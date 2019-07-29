'''
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''


class Solution:
	def longestPalindrome(self, s: str) -> str:        
		sarray = [c for c in s]
		longest = [-1,-1]
		
		lastOccurence = dict()
		prevSameChar = [-1]*len(s)
		
		
		for i in range(len(sarray)):
			ch = sarray[i]
			prevSameChar[i] = lastOccurence.get(ch, -1)
			lastOccurence[ch] = i
			
			if self.isPalindrome(sarray[:i+1]):
				longest = [0,i+1]
			else:
				start=prevSameChar[i]
				while start != -1:
					if self.isPalindrome(sarray[start:i+1]) and i+1-start > longest[1]-longest[0]:
						longest = [start,i+1]
					start = prevSameChar[start]
		return "".join(sarray[longest[0]:longest[1]])
			
			
			
	def isPalindrome(self, s):
		return s == s[::-1]