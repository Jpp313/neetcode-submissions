class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        min_num = 0
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            # left sort
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1                                                        
        
        return nums[l]