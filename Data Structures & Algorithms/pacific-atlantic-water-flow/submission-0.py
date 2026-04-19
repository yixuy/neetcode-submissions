class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #  cell to a neighboring cell with height equal or lower
        # >= neigh
        R = len(heights)
        C = len(heights[0]) 

        def is_valid(x, y, visit):
            return 0 <= x < len(heights) and 0 <= y < len(heights[0]) and (x, y) not in visit

        pac, atl = set(), set()
        direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        def dfs(r, c, visit, prev_h ):
            if not is_valid(r, c, visit) or heights[r][c] < prev_h:
                return 

            visit.add((r, c))
            for dx, dy in direction:
                dfs(dx + r, dy + c, visit, heights[r][c])

        for c in range(C):
            dfs(0, c , pac, heights[0][c])
            dfs(R-1, c , atl, heights[R-1][c])

        for r in range(R):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, C-1, atl, heights[r][C-1])

        res = []
        for r in range(R):
            for c in range(C):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res
