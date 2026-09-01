class Solution:
    def trap(self, height: List[int]) -> int:
        
        i = 0
        j = len(height) - 1
        total = 0
        max_water = 0
        while i < j:
            if height[i] < height[j]:
                i += 1
                max_water = max(max_water, height[i])
                total += max_water - height[i]
            else:
                j -= 1
                max_water = max(max_water, height[j])
                total += max_water - height[j]

        return total - 1