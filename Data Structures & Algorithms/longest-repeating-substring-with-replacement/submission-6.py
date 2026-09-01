class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        i = 0
        max_window_size = 0
        freq = {}
        for j in range(len(s)):
            freq[s[j]] = 1 + freq.get(s[j], 0)

            if (j - i + 1) - max(freq.values()) > k:
                freq[s[i]] -= 1
                i += 1
            max_window_size = (j - i + 1)

        return max_window_size