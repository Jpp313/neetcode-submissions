class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            # left sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]: # if target between
                    r = mid - 1
                else:
                    l = mid + 1
            # right sorted
            if nums[r] >= nums[mid]: 
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
