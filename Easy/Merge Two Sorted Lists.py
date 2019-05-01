'''
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		if not l1 and not l2: return None
		if not l1: return l2
		if not l2: return l1
		head = l1 if l1.val <= l2.val else l2
		
		walker1 = l1
		walker2 = l2
		
		
		if walker2.val < walker1.val:
			after2 = walker2.next
			after1 = walker1
			walker1 = walker2
			walker1.next = after1
			walker2 = after2

		before1 = walker1
		walker1 = walker1.next
		
		
		while walker1 and walker2:
			if walker2.val < walker1.val:
				after2 = walker2.next
				before1.next = walker2
				before1.next.next = walker1
				
				walker1 = before1.next
				walker2 = after2
				
			before1 = walker1
			walker1 = walker1.next
				
				

		walker1 = before1
		while walker2:
			walker1.next = walker2
			walker1 = walker1.next
			walker2 = walker2.next
		return head
	