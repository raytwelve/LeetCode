'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given a linked list, remove the n-th node from the end of list and return its head.
Note:
Given n will always be valid.
Follow up:
Could you do this in one pass?
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		length = 0
		node = head
		while node:
			length += 1
			node = node.next
		nstart = length - n
		
		if nstart == 0:
			head = head.next
			return head
		
		node = head
		count = 1
		while count < nstart:
			count += 1
			node = node.next
		node.next = node.next.next
		return head



# recursive alternative
class Solution:
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		index = -1
		node = self.untilTheEnd(head, n, index)
		
		if not node:
			return head.next
		else:
			node.next = node.next.next
			return head
		
		
	def untilTheEnd(self, node, n, index):
		index += 1
		if node == None:
			return index, None
		
		length, noode = self.untilTheEnd(node.next, n, index)
		target = length - n
		if index == 0:
			if target == 1: return node
			else: return noode
		else:
			if target == index + 1: return length, node
			else: return length, noode
