class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 1
        max_profit = 0
        leftmin = float("infinity")
        for r in range(len(prices)):
            leftmin = min(leftmin, prices[l])
            if leftmin < prices[r]: # make a profit
                max_profit = max(max_profit, prices[r] - leftmin)
            
            l += 1
            

        return max_profit