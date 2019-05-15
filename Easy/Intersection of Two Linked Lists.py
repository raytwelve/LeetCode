'''
https://leetcode.com/problems/intersection-of-two-linked-lists/

Write a program to find the node at which the intersection of two singly linked lists begins.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB: return None
        alist = self.listify(headA)
        
        node = headB
        while node:
            if node in alist:
                return node
            node = node.next
        return None
        
        
        
    def listify(self, node):
        results = set()
        while node:
            results.add(node)
            node = node.next
        return results