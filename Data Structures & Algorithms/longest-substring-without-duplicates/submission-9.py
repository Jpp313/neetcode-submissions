class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0

        mp = {}

        max_len = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(l , mp[s[r]] + 1)
            mp[s[r]] = r
            max_len = max(max_len, r - l + 1)

        return max_len