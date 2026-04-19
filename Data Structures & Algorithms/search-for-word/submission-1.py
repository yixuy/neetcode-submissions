class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.res = False 
        def is_valid(x,y):
            return 0 <= x < len(board) and 0 <= y < len(board[0]) and (x, y) not in visit
        def dfs(x, y, visit, temp):
            if temp == word:
                self.res = True 
                return
            if len(temp) > len(word):
                return 

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_x = dx + x
                next_y = dy + y 

                if is_valid(next_x, next_y):
                    visit.add((next_x, next_y))
                    dfs(next_x, next_y, visit, temp + board[next_x][next_y])
                    visit.remove((next_x, next_y))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if not self.res and board[i][j] == word[0]:
                    visit = set()
                    visit.add((i, j))
                    dfs(i, j, visit, board[i][j])

        return self.res 