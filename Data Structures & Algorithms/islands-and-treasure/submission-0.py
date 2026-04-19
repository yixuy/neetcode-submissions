class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

        directions = [[1,0], [-1,0], [0, 1], [0, -1]]
        q = collections.deque()
        INF = 2147483647

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
    
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for direct in directions:
                    if r + direct[0] in range(len(grid)) and c + direct[1] in range(len(grid[0])) and grid[r + direct[0]][ c + direct[1] ]== INF:
                        grid[r + direct[0]][ c + direct[1] ] = grid[r][c] + 1
                        q.append((r + direct[0], c + direct[1] ))
                    
                