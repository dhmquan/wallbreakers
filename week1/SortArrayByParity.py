class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        nextEvenPos = 0
        #return a new array instead of in-place
        out = A.copy()
        for i in range(len(out)):
            if out[i] % 2 == 0:
                out[i], out[nextEvenPos] = out[nextEvenPos], out[i]
                nextEvenPos += 1
                
        return out