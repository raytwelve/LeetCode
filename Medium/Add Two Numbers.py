'''
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		v1 = 0 if not l1 else l1.val
		v2 = 0 if not l2 else l2.val
		summ = (v1 + v2) % 10
		carry = (v1 + v2) // 10
		head = ListNode(summ)
		node = head
		l1 = l1.next
		l2 = l2.next
		
		while l1 or l2:
			v1 = l1.val if l1 else 0
			v2 = l2.val if l2 else 0
			summ = (v1 + v2 + carry) % 10
			carry = (v1 + v2 + carry) // 10
			node.next = ListNode(summ)
			node = node.next
			l1 = None if not l1 else l1.next
			l2 = None if not l2 else l2.next
		if carry > 0:
			node.next = ListNode(carry)
		return head