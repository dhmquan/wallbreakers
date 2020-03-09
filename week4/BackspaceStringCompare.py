class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_S = []
        stack_T = []
        
        for c in S:
            if c == "#":
                if len(stack_S):
                    stack_S.pop()
            else:
                stack_S.append(c)
                
        for c in T:
            if c == "#":
                if len(stack_T):
                    stack_T.pop()
            else:
                stack_T.append(c)
                
        return ''.join(stack_S) == ''.join(stack_T)