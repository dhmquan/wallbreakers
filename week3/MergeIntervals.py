class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        sorted_ints = sorted(intervals, key = lambda x: x[0])
        
        out = []
        prev_int = sorted_ints[0]
        for interval in sorted_ints[1:]:
            if interval[0] <= prev_int[1]:
                prev_int = [prev_int[0], max(prev_int[1], interval[1])]
                
            else:
                out.append(prev_int)
                prev_int = interval
                
        out.append(prev_int)
        return out