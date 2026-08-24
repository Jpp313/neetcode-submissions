class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        freq = {}
        l = 0
        max_length = 0
       
        for r in range(len(s)):


            if s[r] in freq:
                l = max(freq[s[r]] + 1, l)
                        
            freq[s[r]] = r
            max_length = max(max_length, r - l + 1)

        return max_length