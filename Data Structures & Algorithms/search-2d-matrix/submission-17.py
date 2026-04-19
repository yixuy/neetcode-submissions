class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        ROW = len(matrix)
        COL = len(matrix[0])
        
        right = ROW * COL - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if matrix[mid // COL][mid % COL] == target:
                return True
            elif matrix[mid // COL][mid % COL] < target:
                left = mid
            else:
                right = mid 
        
        if matrix[left // COL][left % COL] == target:
            return True
        if matrix[right // COL][right % COL] == target:
            return True
        
        return False
        