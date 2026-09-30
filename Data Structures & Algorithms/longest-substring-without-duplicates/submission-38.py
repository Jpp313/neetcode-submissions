class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        store = {}

        l = 0
        max_length = 0
        for r in range(len(s)):

            if store and s[r] in store:
                l = max(l, store[s[r]])

            max_length = max(max_length, r - l)

            store[s[r]] = r
            
        return max_length