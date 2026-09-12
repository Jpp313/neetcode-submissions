class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 0
        r = max(piles)

        hours = 0
        # adjust eating rate (mid) up or down if we eat too fast or too slow
        while l <= r:
            k = l + (r - l) // 2
            for p in piles:
                hours += math.ceil(p / k)
                
            
            if hours < h: # ate too fast
                r = k
            elif hours > h: # ate too slow
                l = k
          
        return k
