'''
https://leetcode.com/problems/reverse-vowels-of-a-string/

Write a function that takes a string as input and reverse only the vowels of a string.
'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s: return ""
        VOWELS = {"a","e","i","o","u","A","E","I","O","U"}
        word = [ch for ch in s]
        
        for i in range(len(word)):
            if word[i] in VOWELS:
                positions.append(i)
        
        for i in range(len(positions)//2):
            lpos = positions[i]
            rpos = positions[-i-1]
            word[lpos], word[rpos] = word[rpos], word[lpos]
        return "".join(word)