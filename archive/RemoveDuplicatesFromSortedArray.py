class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        prev = nums[0]
        cur = 1
        for x in nums[1:]:
            if x != prev:
                nums[cur] = x
                prev = x
                cur += 1
        return cur
        