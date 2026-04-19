class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def is_valid(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1"

        def bfs(x, y):
            q = deque([(x, y)])

            while q:
                curr_x, curr_y = q.popleft()

                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    next_x, next_y = curr_x + dx, curr_y + dy

                    if is_valid(next_x, next_y):
                        q.append((next_x, next_y))
                        grid[next_x][next_y] = 0

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)

        return count 