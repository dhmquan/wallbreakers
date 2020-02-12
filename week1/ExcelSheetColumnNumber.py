from functools import reduce
class Solution:
    def titleToNumber(self, s: str) -> int:
        letters = [ord(c) - 64 for c in list(s)]
        return reduce(lambda x, y: x * 26 + y, letters)