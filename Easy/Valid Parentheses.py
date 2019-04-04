'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.


'''

class Solution:
    def isValid(self, s: str) -> bool:
        if s == None or len(s) % 2 == 1: return False
        if len(s) == 0: return True
        
        stack = []
        compliments = {')':'(', ']': '[', '}':'{'}
        for i in range(len(s)):
            curr = s[i]
            if curr in compliments.values():
                stack.append(curr)
            else:
                if len(stack) == 0 or stack[-1] != compliments[curr]: return False
                stack.pop()
        return len(stack) == 0