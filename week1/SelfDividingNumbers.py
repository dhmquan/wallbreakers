class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        out = []
        for x in range(left, right + 1):
            if self.isDividingNumber(x):
                out.append(x)
                
        return out
        
    def isDividingNumber(self, x: int) -> bool:
        leftToParse = x
        
        while leftToParse != 0:
            digit = leftToParse % 10
            if (digit == 0) or (x % digit != 0):
                return False
            leftToParse //= 10
            
        return True