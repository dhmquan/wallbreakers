import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)
        
        for i in range(len(s)):
            char = s[i]
            if counter[char] == 1:
                return i
            
        return -1