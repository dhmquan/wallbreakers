class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        bag = {}
        for c in s:
            if c in bag:
                bag[c] += 1
            else:
                bag[c] = 1
        
        for c in t:
            if c in bag:
                bag[c] -= 1
                if bag[c] == 0:
                    del bag[c]
            else:
                return False
            
        return not bag