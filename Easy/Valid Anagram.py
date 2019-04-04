'''
Given two strings s and t , write a function to determine if t is an anagram of s.
Note:
You may assume the string contains only lowercase alphabets.
Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

https://leetcode.com/problems/valid-anagram/
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (s == None and t == None) or s == None or t == None or len(s) != len(t):
            return False
        return sorted(list(s)) == sorted(list(t))
