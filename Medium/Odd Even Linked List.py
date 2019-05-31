'''
https://leetcode.com/problems/odd-even-linked-list/

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
'''

class Solution:
	def oddEvenList(self, head: ListNode) -> ListNode:
		if not head: return head
		node1 = head
		head2 = head.next
		node2 = head2
		while node1.next and node2.next:
			node1.next = node1.next.next
			node2.next = node2.next.next
			node1 = node1.next
			node2 = node2.next
		node1.next = head2
		return head