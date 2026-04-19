class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # first row becacome last col
        l, r = 0, len(matrix) - 1
       
            
        while l < r:
            for i in range(r-l):
                top, buttom  = l,r 

                topLeft = matrix[top][l+i]

                matrix[top][l+i] =  matrix[buttom-i][l]

                matrix[buttom-i][l] = matrix[buttom][r-i] 
                 
                matrix[buttom][r-i] = matrix[top+i][r]

                matrix[top+i][r] = topLeft
            l += 1
            r -= 1