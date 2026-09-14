class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        min_num = 0
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            # left sort
            if nums[r] < nums[l]:
                l = mid + 1
            else:
                r = mid 
        
        return nums[l] - 1