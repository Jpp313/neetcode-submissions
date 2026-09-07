class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        i = 0

        j = len(matrix) - 1
        mid = (i + j) // 2
        while i < j:

            if target < matrix[mid][0]:
                mid -= 1
            elif target > matrix[mid][-1]:
                mid += 1
            elif target in matrix[mid]:
                return True
            else:
                return False
            