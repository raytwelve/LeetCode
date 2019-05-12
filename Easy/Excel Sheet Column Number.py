'''
https://leetcode.com/problems/excel-sheet-column-number/

Given a column title as appear in an Excel sheet, return its corresponding column number.
'''

class Solution:
    def titleToNumber(self, s: str) -> int:
        sum = 0
        for i in range(len(s)):
            # read backwards
            ch = s[-(i+1)]
            sum += (ord(ch) - ord('A') + 1) * 26**i
        return sum