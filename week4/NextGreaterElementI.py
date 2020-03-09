class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dct = {}
        stack = []
        
        for x in nums2:
            while len(stack) and x > stack[-1]:
                dct[stack.pop()] = x
                
            stack.append(x)
            
        return [(-1 if x not in dct else dct[x]) for x in nums1]