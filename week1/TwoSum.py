class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dct = {}
        
        '''
        The same as:
        for i in range(len(nums)):
            n = nums[i]
            ...
        '''
        for i, n in enumerate(nums):
            m = target - n
            if m in dct:
                return [dct[m], i]
            
            else:
                dct[n] = i