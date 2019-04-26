'''
https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        salnumlower = ''.join(filter(str.isalnum, s.lower()))
        return salnumlower == salnumlower[::-1]
