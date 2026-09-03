class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        window = {}
        max_size = 0
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            size_window = r - l + 1

            if size_window - max(window.values()) >= k:
                max_size = max(max_size, size_window)
                l += 1
                
        return max_size
