'''
https://leetcode.com/problems/linked-list-cycle/

Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?
'''



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def hasCycle(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		if not head: return False
		walk1 = head
		walk2 = head.next
		while walk1 and walk2:
			if walk1 == walk2: return True
			walk1 = walk1.next
			walk2 = walk2.next.next if walk2.next else walk2.next

		return False