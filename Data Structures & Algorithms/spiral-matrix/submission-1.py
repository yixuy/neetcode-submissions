class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        ROW = len(matrix)
        COL = len(matrix[0])
        RIGHT = COL 
        BUTTOM = ROW 
        LEFT = 0
        TOP = 0
        
        while len(res) < ROW * COL:
            for c in range(LEFT, RIGHT):
                res.append(matrix[TOP][c])
            TOP += 1
            if len(res) >= ROW * COL:
                break

            for r in range(TOP, BUTTOM):
                res.append(matrix[r][RIGHT - 1])
            RIGHT -= 1 
            if len(res) >= ROW * COL:
                break
   
            for c in range(RIGHT - 1, LEFT - 1, -1):
                res.append(matrix[BUTTOM - 1][c])
            BUTTOM -= 1
            if len(res) >= ROW * COL:
                break

            for r in range(BUTTOM - 1, TOP - 1, -1):
                res.append(matrix[r][LEFT])
            LEFT += 1
            if len(res) >= ROW * COL:
                break

        return res