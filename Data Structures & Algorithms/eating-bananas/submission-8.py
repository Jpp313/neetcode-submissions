class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        res = r
        # adjust eating rate (mid) up or down if we eat too fast or too slow
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / k)
            
            if hours <= h: # ate too fast
                res = k
                r = k - 1
            elif hours > h: # ate too slow
                l = k + 1
          
        return res
