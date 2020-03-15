# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.helper(root)[0]
        
    def helper(self, node):
        if not node:
            return (0, 0)
        
        left_diam, left_h = self.helper(node.left)
        right_diam, right_h = self.helper(node.right)
        
        diam_with_node = 0
        if left_h > 0:
            diam_with_node += left_h
        if right_h > 0:
            diam_with_node += right_h
            
        node_diam = max(left_diam, right_diam, diam_with_node)
        return (node_diam, max(left_h, right_h) + 1)