class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        i = 0
        output = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j < k:
                cur = nums[i] + nums[j] + nums[k]
                if cur < 0:
                    j += 1
                elif cur > 0:
                    k -= 1
                else:
                    output.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
        return output 