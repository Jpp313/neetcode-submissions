class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix) 
        cols = len(matrix[0])

        l = 0
        r = (rows * cols)  - 1

        while l <= r:
            mid = l + (r - l) // 2
            ROWS = mid // cols
            COLS = mid % cols
        
            if target < matrix[ROWS][COLS]:
                r = mid - 1
            elif target > matrix[ROWS][COLS]:
                l = mid + 1
            else:
                return True
        return False