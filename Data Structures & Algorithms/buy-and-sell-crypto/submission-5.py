class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        i = 0
        j = len(prices) - 1

        while i < j:

            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
          
            if prices[i] > prices[j]:
                i += 1
            else:
                j -= 1

        return max_profit