class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0

        l = 0

        index_dict = {}
        for r in range(len(s)):

            if s[r] in index_dict:
                l = max(l, index_dict[s[r]] + 1) # new pos based off old position + 1 to move ahead


            index_dict[s[r]] = r
            length = (r - l + 1)
            max_length = max(max_length, length)

        return max_length