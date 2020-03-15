"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack = [root]
        out = []
        while len(stack):
            curr = stack.pop()
            out.append(curr.val)
            for c in curr.children:
                stack.append(c)
                
        return out[::-1]