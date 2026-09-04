class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        i = 0
        j = len(nums) - 1
        mid = (i + j + 1) // 2

        if nums[mid] == target:
            return mid
        while i < j:
            
            if target < nums[mid]:
                j = mid - 1
                mid = (i + j) // 2
            if target > nums[mid]:
                i = mid + 1
                mid = (i + j) // 2
            if target == nums[mid]:
                return mid

            
        return -1

            
                