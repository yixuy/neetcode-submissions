class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # find the location of 0

        index = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    index.append((i, j))

        
        for (row, col) in index:
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
            for j in range(len(matrix)):
                matrix[j][col] = 0