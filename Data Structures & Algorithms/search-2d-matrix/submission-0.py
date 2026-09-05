class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        mid = (l + r) // 2
        while l <= r:
            if target in matrix[mid]:
                return True
            elif target < matrix[mid][0]:
                mid -= 1
            elif target > matrix[mid][-1]:
                mid += 1
            else:
                return False
                
                