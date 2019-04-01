'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = None
        carry = 1
        for i in range(-1, -len(digits)-1, -1):
            num = digits[i] + carry
            carry = num // 10
            digits[i] = num % 10
        if carry == 1:
            digits.insert(0, carry)
        return digits