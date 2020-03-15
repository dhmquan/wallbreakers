# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        return self.helper(root)[0]
        
    def helper(self, node):
        if not node:
            return (0, 0)
        
        l_path, l_h = self.helper(node.left)
        r_path, r_h = self.helper(node.right)
        
        path_with_l_and_node = 0
        path_with_r_and_node = 0
        path_that_has_node = 0
        if node.left and node.left.val == node.val:
            path_with_l_and_node += l_h + 1
            path_that_has_node += l_h + 1
        if node.right and node.right.val == node.val:
            path_with_r_and_node += r_h + 1
            path_that_has_node += r_h + 1
            
        return (max(l_path, r_path, path_that_has_node),
                max(path_with_l_and_node, path_with_r_and_node))