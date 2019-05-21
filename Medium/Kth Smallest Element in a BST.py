'''
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        node = root
        _, kth = self.go(root, 0, k)
        return kth.val
        
    def go(self, node, count, k):
        if node.left:
            count, leftnode = self.go(node.left, count, k)
            if count == k: return count, leftnode
            
        count += 1
        if count == k:
            return count, node
        
        if node.right:
            count, rightnode = self.go(node.right, count, k)
            if count == k: return count, rightnode
            
        return count, node