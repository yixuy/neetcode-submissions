class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [[0,1], [1,0], [0, -1], [-1, 0]]
        r = len(board)
        c = len(board[0])
        path = set()
        def backtrack(row, col, i):
            if i == len(word):
                return True
            
            if row >= r or row < 0 or col < 0 or col >= c or board[row][col] != word[i] or (row, col) in path:
                return False
            res = False
            path.add((row, col))
            for direction in dirs:
                next_row = row + direction[0]
                next_col = col + direction[1]
                res = res or backtrack(next_row, next_col, i+1)
            path.remove((row, col))
            return res 

        for i in range(r):
            for j in range(c):
                if backtrack(i, j, 0):
                    return True

        return False 