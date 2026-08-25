class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
       

        max_length = 0
        for i in range(len(nums)):

            if (nums[i] - 1) not in nums:
                length = 0
                j = 0
                while (nums[i] + j) in nums:
                    length += 1
                    j += 1
            
                max_length = max(max_length, length)

            

            
        return max_length

