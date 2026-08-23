class Solution:
    def trap(self, height: List[int]) -> int:
        
        i = 0 
        j = len(height) - 1
        leftMax = height[i]
        rightMax = height[j]
        total = 0 
        while i < j:
            if leftMax < rightMax:
                i += 1
                leftMax = max(leftMax, height[i])
                total += leftMax - height[i] 
            else:
                j -= 1
                rightMax = max(rightMax, height[j])
                total += rightMax - height[r]
        return total