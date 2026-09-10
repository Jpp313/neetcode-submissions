class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        hours = 0
        res = r
        while l <= r:
            k = (l + r) // 2
            for p in piles: # how long to eat each pile
                hours += math.ceil(float(p) / k)
            if hours <= h: # ate too fast so we lower the eating rate
                res = k
                r = k - 1
            elif hours > h: # ate too slow so we increase the eating rate
                l = k + 1
        return res