class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        dirctions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        ROW, COL = len(board), len(board[0])
        # check the surround 
        def is_valid(x, y):
            return 0 <= x < ROW and 0 <= y < COL and board[x][y] == "O"
        
        def bfs():
            q = deque([])

            for row in range(ROW):
                for col in range(COL):
                    if row == 0 or row == ROW - 1 or col == 0 or col == COL - 1 and board[row][col] == "O":
                        q.append((row, col))
            while q:
                curr_x, curr_y = q.popleft()
                if board[curr_x][curr_y] == "O":
                    board[curr_x][curr_y] = "T"

                    for dx, dy in dirctions:
                        next_x = dx + curr_x
                        next_y = dy + curr_y

                        if is_valid(next_x, next_y):
                            q.append((next_x,next_y))

        bfs()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"



