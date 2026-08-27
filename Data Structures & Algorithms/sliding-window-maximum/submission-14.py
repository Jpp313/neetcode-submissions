class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        q = deque()
        l = 0
        r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: # remove all old smaller values entirely starting from the back because we only care about maxes no need to keep old lower vals
                q.pop()
            q.append(r)

            if l > q[0]: # remove expired values as our left window slides
                q.popleft()
            
            if (r + 1) >= k: # add the first val in deque when our window reaches correct size
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output


