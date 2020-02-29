class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        
        points = sorted(points, key = lambda x: x[0])
        
        arrows = 1
        start, end = points[0]
        
        for pt in points[1:]:
            pt_start, pt_end = pt
            if pt_start <= end:
                start = max(start, pt_start)
                end = min(end, pt_end)
            
            else:
                arrows += 1
                start = pt_start
                end = pt_end
                
        return arrows
        