class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(x):
            if x < 2:
                return 1
            
            if x in memo:
                return memo[x]
            
            res = helper(x-1) + helper(x-2)
            memo[x] = res
            return res
        
        return helper(n)