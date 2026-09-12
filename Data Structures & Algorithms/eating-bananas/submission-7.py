class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 0
        r = max(piles)

        hours = 0
        # adjust eating rate (mid) up or down if we eat too fast or too slow
        while l <= r:
            if (l + (r - l) // 2) == 0:
                break
            k = l + (r - l) // 2
            for p in piles:
                hours += math.ceil(p / k)
                
            if hours < h: # ate too fast
                r = k - 1
            elif hours > h: # ate too slow
                l = k + 1
          
        return k
