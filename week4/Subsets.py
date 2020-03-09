class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = [[]]
        for x in nums:
            cur_l = len(power_set)
            for i in range(cur_l):
                power_set.append(power_set[i] + [x])
                
        return power_set