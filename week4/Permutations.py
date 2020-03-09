class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        self.helper(nums, [], out)
        return out
        
    def helper(self, nums, cur_set, out):
        if not len(nums):
            out.append(cur_set)
            
        for i in range(len(nums)):
            self.helper(nums[:i] + nums[i + 1:], cur_set + [nums[i]], out)