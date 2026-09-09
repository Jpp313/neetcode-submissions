class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        rows = len(matrix) 
        cols = len(matrix) 
        while l <= r:
            m = (l + r) // 2

            rows = m // 4
            cols = m % 4

            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            elif target in matrix[m]:
                return True
            else:
                return False

        return False