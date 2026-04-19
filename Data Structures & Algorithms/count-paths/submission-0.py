class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = []
        for i in range(m):
            memo.append([0] * n)
        memo[0][0] = 1 


        def dp(x, y):
            if memo[x][y] != 0:
                return memo[x][y]
            if 0 <= x - 1 < m:
                memo[x][y] += dp(x-1, y)
            if 0 <= y - 1 < n:
                memo[x][y] += dp(x, y-1)
                
            return memo[x][y]

        dp(m-1, n-1)
        return memo[m-1][n-1]