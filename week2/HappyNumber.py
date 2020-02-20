class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = {}
        
        while n not in numbers:
            numbers[n] = True
            
            new_n = 0
            for i in range(len(str(n))):
                new_n += (n // 10 ** i % 10) ** 2
            
            if new_n == 1:
                return True
            
            n = new_n
        
        return False