# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [(root, False)]
        
        out = 0
        while len(stack):
            curr, isLeft = stack.pop()
            if not curr.left and not curr.right and isLeft:
                out += curr.val
                
            if curr.left:
                stack.append((curr.left, True))
            if curr.right:
                stack.append((curr.right, False))
                
        return out