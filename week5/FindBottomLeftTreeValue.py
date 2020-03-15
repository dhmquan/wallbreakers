# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = deque()
        
        out = root.val
        q.append(root)
        q.append(None)
        
        while len(q):
            node = q.popleft()
            
            if not node:
                #reached the end queue
                if not len(q):
                    break
                
                out = q[0].val
                q.append(None)
                continue
                
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        return out