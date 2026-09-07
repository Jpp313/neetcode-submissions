class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()

        l = 0

        for r in range(len(nums)):
            
            while q and nums[q[0]] < nums[r]: # check if we should pop an old max if our cur r is bigger
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            
            if (r - l + 1) == k:
                output.append(nums[q[0]])
                l += 1                   
        return output
