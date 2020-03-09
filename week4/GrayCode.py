class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        out = ['']
        for _ in range(n):
            #every time a new bit is added, the sequence doubles in length,
            #and mirrors
            left = out[:]
            right = out[::-1]
            out = [('0' + code) for code in left] + [('1' + code) for code in right]
            
        return [int(code, 2) for code in out]