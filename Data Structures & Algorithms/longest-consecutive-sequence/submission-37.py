class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)

        max_seq = 0
        for num in numSet:
            if num - 1 in numSet:
                continue
            length = 0
            while num + length in numSet:
                length += 1
            max_seq = max(max_seq,length)
        return max_seq