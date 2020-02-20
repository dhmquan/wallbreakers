import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cs = collections.Counter(s)
        ct = collections.Counter(t)
        
        out = ct - cs
        #Is there a better way to do this?
        return out.most_common()[0][0]