import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        c = collections.Counter(s)
        
        most_commons = c.most_common()
        
        substrings = [item[0] * item[1] for item in most_commons]
        return ''.join(substrings)