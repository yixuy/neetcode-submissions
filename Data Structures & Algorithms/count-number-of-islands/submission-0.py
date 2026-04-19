class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # result = []
        # def backtrack(路径, 选择列表):
        #     if 满足结束条件:
        #         result.add(路径)
        #         return
            
        #     for 选择 in 选择列表:
        #         做选择
        #         backtrack(路径, 选择列表)
        #         撤销选择
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        result = [] 
        islands = 0
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return 
            grid[r][c] = '0'
            for dr, dc in directions:
                dfs(dr+r, dc+c) 


        for r in range(rows):
            for c in range(cols):
                if  grid[r][c] == '1':
                    dfs(r,c)
                    islands += 1
        return islands
                    


        return islands

