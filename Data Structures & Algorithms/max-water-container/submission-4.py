class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i = 0
        j = len(heights) - 1
        max_area = 0

        while i < j:

            height = min(heights[i],heights[j])
            width = abs(i - j)
            area = height * width
            if height == heights[i]:
                i += 1
            if height == heights[j]:
                j -= 1
            max_area = max(max_area,area)
            
            
        
        return max_area