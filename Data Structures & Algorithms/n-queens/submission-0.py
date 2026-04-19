class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        col = set()
        posDiag = set()
        negDiag = set()
        board = [['.'] * n for i in range(n)]

        def dfs(index):
            if index == n:
                copy = []
                for row in board:
                    copy.append("".join(row))
                self.res.append(copy)
                return 
            
            for i in range(n):
                if i in col or (index + i ) in posDiag or (index - i) in negDiag:
                    continue
                col.add(i)
                posDiag.add(index + i)
                negDiag.add(index - i)
                board[index][i] = "Q"
                dfs(index + 1)
                col.remove(i)
                posDiag.remove(index + i)
                negDiag.remove(index - i)
                board[index][i] = "."

        dfs(0)  
        return self.res          
                
