class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0

        freq_dict = {}
        max_len = 0

        for r in range(len(s)):
            c = s[r]

            if c in freq_dict:
                l = max(l, freq_dict[c] + 1)

            freq_dict[c] = r

            max_len = max(max_len, r - l + 1)

        return max_len

            


