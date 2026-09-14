class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        min_num = 0
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            # left sort
            if nums[l] < nums[r]:
                if nums[l] <= nums[mid]:
                    r = mid - 1
            elif nums[r] < nums[l]:
                if nums[mid] >= nums[r]:
                    l = mid + 1
                else:
                    l = mid                                                           
        
        return nums[l]