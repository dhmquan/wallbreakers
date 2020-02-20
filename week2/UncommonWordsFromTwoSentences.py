class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        common = set()
        uncommon = set()
        list_A = A.split(" ")
        list_B = B.split(" ")
        
        for word in (list_A + list_B):
            if word in common:
                continue
                
            if word in uncommon:
                uncommon.discard(word)
                common.add(word)
            else:
                uncommon.add(word)
        
        return list(uncommon)