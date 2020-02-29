class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        
        t_idx = 0
        for c in s:
            while t_idx < len(t):
                #print("comparing " + c + " and " + t[t_idx])
                if c == t[t_idx]:
                    t_idx += 1
                    break
                    
                t_idx += 1
            if t_idx == len(t) and c != t[t_idx - 1]:
                return False
            
        return True