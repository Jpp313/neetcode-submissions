class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        n = len(heights)
        max_area = 0

        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]): # means we cannot extend rectangle
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                area = height * width
                max_area = max(max_area, area)
            stack.append(i)
        return max_area