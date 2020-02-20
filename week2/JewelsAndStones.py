class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dct = {}
        for c in J:
            dct[c] = 0
        
        for c in S:
            if c in dct:
                dct[c] += 1
                
        return sum(dct.values())