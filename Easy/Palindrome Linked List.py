'''
https://leetcode.com/problems/palindrome-linked-list/

Given a singly linked list, determine if it is a palindrome.
Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def isPalindrome(self, head: ListNode) -> bool:
		if not head: return True
		length = 0
		walker = head
		
		stack = list()
		
		while walker:
				length += 1
				stack.append(walker.val)
				walker = walker.next
		
		walker = head
		for i in range(length//2+1):
			top = stack.pop()
			if walker.val != top: return False
			walker = walker.next
		return True