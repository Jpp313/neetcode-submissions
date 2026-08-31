class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i = 0
        j = 1
        max_profit = 0
        while j < len(prices):
            if prices[i] < prices[j]: # if we can make a profit
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
            else:
                i = j

            j += 1
        return max_profit
