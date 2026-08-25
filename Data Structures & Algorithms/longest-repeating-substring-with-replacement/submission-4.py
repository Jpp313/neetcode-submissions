class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_length = 0
        i = 0
        
        freq = {}
        for j in range(len(s)):
            freq[s[j]] = 1 + freq.get(s[j], 0)

            length = (j - i + 1)

            if (length - max(freq.values()) > k):
                freq[s[i]] -= 1
                i += 1

            else:
                max_length = max(max_length, length)

        return max_length