'''
https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list.
Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
# class ListNode:
#	 def __init__(self, x):
#		 self.val = x
#		 self.next = None

class Solution:
	def reverseList(self, head: ListNode) -> ListNode:
		# iterative
		frontwalker = head
		backwalker = None

		while frontwalker != None:
			temppointer = frontwalker.next
			frontwalker.next = backwalker
			backwalker = frontwalker
			frontwalker = temppointer
		head = backwalker
		return head