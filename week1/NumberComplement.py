class Solution:
    def findComplement(self, num: int) -> int:
        binary = format(num, 'b')
        mask = (2 ** len(binary)) - 1
        return num ^ mask