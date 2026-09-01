class Solution:
    def trap(self, height: List[int]) -> int:
        
        i = 0
        j = len(height) - 1
        total = 0
        leftmax = 0
        rightmax = 0
        while i < j:
            if height[i] < height[j]:
                leftmax = max(leftmax, height[i])
                total += leftmax - height[i]
                i += 1

            else:
                rightmax = max(rightmax, height[j])
                total += rightmax - height[j]
                j -= 1

        return total