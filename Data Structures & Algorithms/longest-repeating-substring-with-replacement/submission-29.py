class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        l = 0
        max_length = 0
        # check size of window - most freq char == k 
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if (r - l + 1) - max(window.values()) <= k:
                max_length = max(max_length, r - l + 1)
            else:
                window[s[l]] -= 1
                l += 1
        return max_length

