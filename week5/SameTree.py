# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack_p = [(p, "r")]
        stack_q = [(q, "r")]
        
        while len(stack_p) and len(stack_q):
            curr_p, pos_p = stack_p.pop()
            curr_q, pos_q = stack_q.pop()
            
            if not curr_p and not curr_q:
                continue
                
            if not curr_p or not curr_q:
                return False
            
            if curr_p.val != curr_q.val or pos_p != pos_q:
                return False
            
            stack_p.append((curr_p.left, "l"))
            stack_p.append((curr_p.right, "r"))
            stack_q.append((curr_q.left, "l"))
            stack_q.append((curr_q.right, "r"))
            
        return not len(stack_p) and not len(stack_q)