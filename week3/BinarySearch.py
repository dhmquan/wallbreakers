class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)
        
    def binary_search(self, nums, lo, hi, x):
        if lo > hi:
            return -1
        
        mid = lo + (hi - lo) // 2
        if x == nums[mid]:
            return mid
        
        if x < nums[mid]:
            return self.binary_search(nums, lo, mid - 1, x)
        else:
            return self.binary_search(nums, mid + 1, hi, x)