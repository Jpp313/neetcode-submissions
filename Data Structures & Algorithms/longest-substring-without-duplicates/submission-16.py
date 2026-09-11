class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        l = 0
        freq_dict = {}
        for r in range(len(s)):
            c = s[r]
            if c in freq_dict:
              l = max(l, freq_dict[c] + 1)
            freq_dict[c] = r
            max_length = max(max_length, r - l + 1)    
        return max_length