class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)
        for i in range(len(nums)):

            j = i + 1
            k = len(nums) - 1
            
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            while j < k:
                cur = nums[i] + nums[j] + nums[k]
                if cur < 0:
                    j += 1
                elif cur > 0:
                    k -= 1
                else:
                    res.append((nums[i],nums[j],nums[k]))
                    j += 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1

        return res