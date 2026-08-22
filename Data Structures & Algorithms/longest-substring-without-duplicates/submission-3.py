class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mp = {}
        left = 0
        res = 0

        for right in range(len(s)):
            if s[right] in mp:
                left = max(mp[right] + 1, left)
            mp[right] = right
            res = max(res,right - left + 1)
        return res