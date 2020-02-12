class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        binary = format(xor, 'b')
        return binary.count('1')