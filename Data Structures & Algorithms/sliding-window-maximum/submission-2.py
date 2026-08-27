class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = 0
        r = 3
        res = []
        while r < len(nums) + 1:

            window = nums[l:r]
            res.append(max(window))
            l += 1
            r += 1

        return res