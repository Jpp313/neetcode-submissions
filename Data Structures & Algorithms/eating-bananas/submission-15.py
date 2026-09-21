class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1 # lowest possible eating rate is 1
        r = max(piles) # max eating rate is max val

        res = 0
        while l <= r:
            k = l + (r - l) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k) # calculate how long to eat all piles by k eating rate
            
            if hours <= h: # ate too fast
                res = k
                r = k - 1
            else: # ate too slow
                l = k + 1

        return res

