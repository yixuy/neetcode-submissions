class Solution:
    def solve(self, board: List[List[str]]) -> None:
        all_circle = []
        ROW = len(board)
        COL = len(board[0])

        def capture_dfs(r, c):
            if r < 0 or c < 0 or r == ROW or c == COL or board[r][c] != "O":
                return 
            board[r][c] = "T"

            capture_dfs(r+1, c)
            capture_dfs(r-1, c)
            capture_dfs(r, c-1)
            capture_dfs(r, c+1)


        # capture unsurrounded regions using DFS

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == "O" and i in [0, ROW-1] or j in [0, COL-1]:
                    capture_dfs(i, j)

        DIR = [[-1, 0], [1, 0], [0, -1], [0, 1] ]
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == "T":
                    board[i][j] = "O"
            
            
            

