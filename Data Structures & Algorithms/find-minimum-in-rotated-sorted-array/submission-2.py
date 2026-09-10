class Solution:
    def findMin(self, nums: List[int]) -> int:
        
       

        l = 0
        r = len(nums) - 1
        min_num = float("infinity")
        while l <= r:
            if nums[l] < nums[r]:
                min_num = min(min_num, nums[l])
                r -= 1
            elif nums[l] > nums[r]:
                min_num = min(min_num, nums[r])
                l += 1
            else:
                l += 1
                r -= 1
        
        if min_num == float("infinity"):
            return nums[0]
        else:
            return min_num