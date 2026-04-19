class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Backtrack
        R = len(board)
        C = len(board[0])
        
        def backtrack(row, col, word, i):
            if i == len(word):
                return True
            
            if row >= R or col < 0 or row < 0 or col >= C or word[i] != board[row][col]:
                return False
            
            board[row][col] = '*'
            res = backtrack(row + 1, col, word, i+1) or backtrack(row, col+1, word, i+1) or backtrack(row - 1, col, word, i+1) or backtrack(row , col - 1, word, i+1)
            board[row][col] = word[i]
            return res 
        res = []
        for word in words:
            for i in range(R):
                for j in range(C):
                    if board[i][j] != word[0]:
                        continue
                    else:
                        if backtrack(i, j, word, 0):
                           if word not in res:
                                res.append(word)
        
        return res