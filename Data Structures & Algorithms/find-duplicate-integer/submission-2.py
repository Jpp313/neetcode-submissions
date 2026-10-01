class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        fast = 1
        slow = 0
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                return nums[slow]
            fast += 2
            slow += 1
        return nums[fast - 1]
            
            
        