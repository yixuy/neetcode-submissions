class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def is_valid(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1
       
        q = deque([])
        visit = set()
        res = []
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2 and (i, j) not in visit:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        level = 0 
        while fresh > 0 and q:
            s = len(q)

            for _ in range(s):
                curr_x, curr_y = q.popleft()
                grid[curr_x][curr_y] = 0

                for dx, dy in [(-1,0), (1, 0), (0, 1), (0, -1)]:
                    next_x, next_y = curr_x + dx, curr_y + dy

                    if is_valid(next_x, next_y) and (next_x, next_y) not in visit:
                        q.append((next_x, next_y))
                        grid[next_x][next_y] = 2
                        fresh -= 1
            level += 1

        return level if fresh == 0 else -1

     
                