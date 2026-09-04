class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 1:
            return 0
        i = 0
        j = len(nums) - 1
        mid = (i + j + 1) // 2
        while i < j:
            
            if target < nums[mid]:
                j = mid - 1
            if target > nums[mid]:
                i = mid + 1
            if target == nums[mid]:
                return mid
            mid = (i + j) // 2
        return -1

            
                