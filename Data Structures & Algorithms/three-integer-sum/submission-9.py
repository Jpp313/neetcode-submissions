class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
       
        nums.sort()
        res = []
        print(nums)
        for k in range(len(nums)):
            i = k + 1
            j = len(nums) - 1
            while i < j:
                summation = nums[k] + nums[i] + nums[j]
                if summation < 0:
                    i += 1
                elif summation > 0:
                    j -= 1
                elif summation == 0:
                    res.append([nums[k], nums[i], nums[j]])
                    break
        return res
