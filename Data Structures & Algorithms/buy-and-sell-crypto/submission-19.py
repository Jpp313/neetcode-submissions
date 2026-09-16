class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 1
        max_profit = 0
        leftmin = float("infinity")
        while r < len(prices):

            leftmin = min(leftmin, prices[l])
            if leftmin < prices[r]: # make a profit

                max_profit = max(max_profit, prices[r] - leftmin)
                r += 1
            else:
                l += 1
                r += 1

        return max_profit