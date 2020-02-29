import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        p_counter = collections.Counter(p)
        window = collections.Counter(s[:len(p)])
        
        out = []
        for i in range(len(s)):
            if len(p_counter - window) == 0:
                out.append(i)
                
            end_i = i + len(p)
            if end_i >= len(s):
                break
                
            window.subtract(s[i])
            window.update(s[end_i])
            
        return out