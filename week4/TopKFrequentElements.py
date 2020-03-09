import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for x in nums:
            if x in dct:
                dct[x] += 1
            else:
                dct[x] = 1
                
        counts = [(-v, k) for k, v in dct.items()]
        heapq.heapify(counts)
        
        out = []
        for i in range(k):
            out.append(heapq.heappop(counts)[1])
        return out