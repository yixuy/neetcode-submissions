class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        import collections
        self.count = 0
        def isValid(new_x, new_y):
            return 0 <= new_x < len(grid) and  0 <= new_y < len(grid[0]) and grid[new_x][new_y] != 0 
        def bfs(x, y):
            queue = deque([(x,y)])
            island_count = 1
            grid[x][y] = 0
            while queue:
                curr_x, curr_y = queue.popleft()
        
                for dx,dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                    new_x = curr_x + dx 
                    new_y = curr_y + dy 

                    if isValid(new_x, new_y):
                        island_count += 1
                        queue.append((new_x, new_y))
                        grid[new_x][new_y] = 0
            return island_count

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = max(bfs(i, j), count)
    
        return count 
            




        