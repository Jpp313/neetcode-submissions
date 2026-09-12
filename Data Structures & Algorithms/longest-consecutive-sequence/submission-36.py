class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)

        res = []
        max_length = 0
        for num in numSet:
            if num - 1 in numSet: # not a sequence
                continue
            length = 0
            while num + length in numSet: # while we see consec frequencies
                length += 1
            max_length = max(max_length, length)

        return max_length
            