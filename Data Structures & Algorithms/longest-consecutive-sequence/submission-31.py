class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort()

        max_length = 0
       
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            length = 0
            j = i
            while nums[j] + 1 in nums:
                length += 1
                j += 1
            max_length = max(max_length, length)
        
        return max_length

