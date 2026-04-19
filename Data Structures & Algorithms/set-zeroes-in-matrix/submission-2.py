class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # find the location of 0

        # index = []

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 0:
        #             index.append((i, j))
        
        # for (row, col) in index:
        #     for i in range(len(matrix[0])):
        #         matrix[row][i] = 0
        #     for j in range(len(matrix)):
        #         matrix[j][col] = 0
       
        # determine which row or col need to be zero
        row_zero = False
        # use the first element to indicate whether it require zero out 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        row_zero = True
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0 

        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if row_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0




