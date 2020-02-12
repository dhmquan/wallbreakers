class Solution:
    def binaryGap(self, N: int) -> int:
        bestGap = 0
        gap = 0
        startCount = False
        
        while N != 0:
            if N & 1:
                if not startCount:
                    startCount = True
                else:
                    gap += 1
                    if gap > bestGap:
                        bestGap = gap
                gap = 0
                    
            else:
                gap += 1
            N >>= 1
            
        return bestGap