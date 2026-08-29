class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        d = deque()
        
        
        for i in range(len(nums)):
            
            val = max(nums[i: k + i])
            d.append(val)
            if val >= d[0]:
                res.append(val)

        return res