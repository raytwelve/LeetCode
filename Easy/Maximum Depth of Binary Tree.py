'''
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.

https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, node, current_level):
        if node == None:
            return current_level
        current_level += 1
        return max(self.traverse(node.left, current_level), self.traverse(node.right, current_level))
    
    def maxDepth(self, root: TreeNode) -> int:
        current_level = 0
        return self.traverse(root, current_level)
