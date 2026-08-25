class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_length = 0
        i = 0
        
        freq = {}
        max_f = 0
        for j in range(len(s)):
            freq[s[j]] = 1 + freq.get(s[j], 0)
            max_f = max(max_f, freq[s[j]])
            length = (j - i + 1)

            if (length - max_f > k):
                freq[s[i]] -= 1
                i += 1

            else:
                max_length = max(max_length, length)

        return max_length