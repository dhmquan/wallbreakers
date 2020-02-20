class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        seen_in_t = set()
        for i in range(len(s)):
            cs = s[i]
            ct = t[i]
            
            if cs not in s_to_t:
                if ct in seen_in_t:
                    return False
                s_to_t[cs] = ct
                seen_in_t.add(ct)
                
            elif s_to_t[cs] != ct:
                return False
            
        return True
                