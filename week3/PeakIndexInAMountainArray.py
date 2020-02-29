class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return self.binarySearch(A, 0, len(A))
        
    def binarySearch(self, A, lo, hi):
        mid = lo + (hi - lo) // 2
        
        left = float("-inf") if mid == 0 else A[mid - 1]
        right = float("-inf") if mid == len(A) - 1 else A[mid + 1]
        x = A[mid]
        if left < x and x > right:
            return mid
        
        elif left < x and x < right:
            return self.binarySearch(A, mid + 1, hi)
        
        else:
            return self.binarySearch(A, lo, mid - 1)