class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        
        indices = {}
        max_length = 0


        
        for r in range(len(s)):

            if s[r] in indices:
               l = max(l , indices[s[r]])
            
            indices[s[r]] = r
            max_length = max(max_length, r - l)

        return max_length

