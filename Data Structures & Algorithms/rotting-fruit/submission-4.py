class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0

        # BFS  
        q = collections.deque()
        count = 0
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            # length = len(q)
            for i in range(len(q)):
                row, col = q.popleft()

                for direct in direction:
                    r = row + direct[0]
                    c = col + direct[1]
                    if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r,c))
                        fresh -= 1
           
            count+=1

        return count if fresh == 0 else -1
        