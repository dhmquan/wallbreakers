class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []
        self.helper(list(range(1, n + 1)), [], out, 0, k)
        return out
        
    def helper(self, nums, cur_combo, out, start_i, k):
        if len(cur_combo) == k:
            out.append(cur_combo)
            
        if start_i == len(nums):
            return
        
        for i in range(start_i, len(nums)):
            self.helper(nums, cur_combo + [nums[i]], out, i + 1, k)