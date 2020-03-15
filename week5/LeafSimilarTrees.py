# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        
        if not root1 or not root2:
            return False
        
        seq1 = self.getLeafValueSequence(root1)
        seq2 = self.getLeafValueSequence(root2)
        
        return seq1 == seq2
        
    def getLeafValueSequence(self, root):
        stack = [root]
        
        out = []
        while len(stack):
            curr = stack.pop()
            
            #found a leaf
            if not curr.left and not curr.right:
                out.append(curr.val)
                
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
                
        return out