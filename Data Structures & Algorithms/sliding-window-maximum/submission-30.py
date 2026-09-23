class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = deque()

        l = 0

        output = []
        for r in range(len(nums)):
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r) # keep track of indices

            if l > q[0]: # went oldest val in deque is stale
                q.popleft()
            
            
            if (r - l + 1) == k: # if we are at the size of the window
                output.append(nums[q[0]])
                l += 1
        
        return output
        
        


