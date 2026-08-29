class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []

        q = deque()

        r = 0
        l = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: # remove smaller values in queue
                q.pop()
            q.append(r)

            if l > q[0]: # if leftmost index is bigger than oldest index 
                q.popleft() # removes stale index
            
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output

