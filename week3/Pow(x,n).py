class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        if n < 0:
            x = 1 / x
            n = n * -1
        
        extra = x if n % 2 == 1 else 1
        return self.myPow(x, n // 2) ** 2 * extra