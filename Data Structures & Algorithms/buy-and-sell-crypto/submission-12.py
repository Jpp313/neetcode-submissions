class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i = 0
        j = 1
        max_profit = 0
        while j < len(prices):

            if prices[i] <= prices[j]:
                current_profit = prices[j] - prices[i]
                print(current_profit)
                max_profit = max(max_profit, current_profit)
                j += 1
            else:
                i += 1
            

        return max_profit