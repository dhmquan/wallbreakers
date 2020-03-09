# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        N -= 1
        if N == 0:
            return [TreeNode(0)]
        
        out = []
        for i in range(1, N, 2):
            for left_node in self.allPossibleFBT(i):
                for right_node in self.allPossibleFBT(N - i):
                    root = TreeNode(0)
                    root.left = left_node
                    root.right = right_node
                    out += [root]
        return out