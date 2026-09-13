class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0
        l = 0
        r = len(heights) - 1
        area = 0
        while l <= r:
            
            if heights[r] > heights[l]:
                
                max_area = max(max_area, (r - l) * heights[l])
                l += 1
            else:
                max_area = max(max_area, (r - l) * heights[r])
                r -= 1

        return max_area

