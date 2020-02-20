class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        
        out = set()
        for x in nums2:
            if x in nums1_set:
                out.add(x)
                
        return list(out)