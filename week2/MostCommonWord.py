import collections
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = paragraph.lower()
        
        words = re.split(r'\W+', p)
        
        counter = collections.Counter(words)
        
        for s in banned:
            counter[s] = 0
            
        return counter.most_common()[0][0]