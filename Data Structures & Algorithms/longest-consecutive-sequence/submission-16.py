class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
       

        max_length = 0
        num_set = set(nums)
        for num in num_set:

            if (num - 1) not in num_set:
                length = 0
                j = 0
                while (num + j) in num_set:
                    length += 1
                    j += 1
            
                max_length = max(max_length, length)

             
        return max_length

