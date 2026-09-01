class Solution:
    def trap(self, height: List[int]) -> int:
        
        i = 0
        j = len(height) - 1
        total = 0
        leftmax = 0
        rightmax = 0
        while i < j:
            if leftmax < rightmax:
                i += 1
                leftmax = max(leftmax, height[i])
                total += leftmax - height[i]
            else:
                j -= 1
                rightmax = max(rightmax, height[j])
                total += rightmax - height[j]

        return total