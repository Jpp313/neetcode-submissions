class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        product = 1
        prefix = 0
        for num in nums:
            prefix = product
            product = prefix * num
            res.append(prefix)

        postfix = 1
        for i in range(len(nums) - 1, -1 , -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res