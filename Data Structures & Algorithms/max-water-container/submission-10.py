class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0
        l = 0
        r = len(heights) - 1
        area = 0
        while l <= r:
            height = min(heights[l],heights[r])
            max_area = max(max_area, (r - l) * height)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1

        return max_area

