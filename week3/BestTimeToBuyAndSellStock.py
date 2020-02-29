class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        profit = 0
        min_p = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > min_p:
                new_profit = prices[i] - min_p
                if new_profit > profit:
                    profit = new_profit
            elif prices[i] < min_p:
                min_p = prices[i]
                
        return profit