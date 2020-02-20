class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        kinds = set(candies)
        return min(len(candies) // 2, len(kinds))