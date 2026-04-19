class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom = 0
        top = len(matrix) - 1

        temp_mid_row = 0
        while bottom <= top :
            temp_mid_row = (bottom + top) // 2 
            if matrix[temp_mid_row][-1] < target:
                bottom = temp_mid_row + 1
            elif matrix[temp_mid_row][0] > target:
                top = temp_mid_row - 1
            else:
                break
        # print(temp_mid_row)
        if not(bottom <= top ):
            return False
        temp_mid_row = (top + bottom ) // 2
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            temp_mid_col = (left + right) // 2 
            if matrix[temp_mid_row][temp_mid_col] < target:
                left = temp_mid_col + 1
            elif matrix[temp_mid_row][temp_mid_col] > target:
                right = temp_mid_col - 1
            else:
                return True
        return False
        