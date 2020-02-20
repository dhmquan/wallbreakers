import collections
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = collections.Counter(range(1, len(nums) + 1))
        c.update(nums)
        
        most_common = c.most_common()
        return[most_common[0][0], most_common[-1][0]]