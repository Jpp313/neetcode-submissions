class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        count = {}
        length = 0
        maxf = 0
        for r in range(len(s)):
            c = s[r]
            count[c] = 1 + count.get(c,0)
            maxf = max(count[c],maxf)

            # see if we fit in k window
            if (r - l + 1) - maxf <= k:
                length = max(length, r - l + 1)
            else:
                count[s[l]]
                l += 1
            
        return length
