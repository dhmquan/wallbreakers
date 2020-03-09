class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        prev = ")"
        
        for c in S:
            if c == "(":
                if prev == "(":
                    stack.append(0)
                
                prev = "("
                
            else:
                if prev == "(":
                    stack.append(1)
                else:
                    total_in_this_parens = 0
                    while stack[-1] != 0:
                        total_in_this_parens += stack.pop()
                    stack.pop()
                    stack.append(total_in_this_parens * 2)
                
                prev = ")"
                
        return sum(stack)