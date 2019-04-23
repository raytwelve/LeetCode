'''
https://leetcode.com/problems/validate-binary-search-tree/

Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# import sys

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        node = root
        if not node: return True
        maxx = sys.maxsize
        minn = -sys.maxsize-1
        
        
        return self.valid(node.left, node.val, minn) and self.valid(node.right, maxx, node.val)
        
            
            
    def valid(self, node, maxx, minn):
        if not node: return True
        
        if node.val < maxx and node.val > minn:
            return self.valid(node.left, node.val, minn) and self.valid(node.right, maxx, node.val)
        else: return False