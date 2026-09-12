class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)

        res = []
        length = 0
        max_length = 0
        for num in numSet:
            if num - 1 in numSet: # not a sequence
                continue
            while num + length in numSet:
                length += 1
            max_length = max(max_length, length)
        return max_length
            