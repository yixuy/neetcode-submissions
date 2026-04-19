class Solution {
    private int ROW, COL;
    private char[][] grid;
    private final int[][] directions = {
        {-1, 0},
        {1, 0},
        {0, -1},
        {0, 1}
    };
    
    public void bfs(int row, int col, char[][] grid){
        Deque<int[]> q = new LinkedList<>();
        q.offerLast(new int[]{row, col});
        grid[row][col] = '0';

        while(!q.isEmpty()){
            int[] curr = q.pollFirst();

            for(int[] dir: directions){
                int newX = dir[0] + curr[0];
                int newY = dir[1] + curr[1];

                if(0 <= newX && newX < ROW && 0 <= newY && newY < COL && grid[newX][newY] == '1'){
                    q.offerLast(new int[]{newX, newY});
                    grid[newX][newY] = '0';
                }
            }
        }
        
    }
    public int numIslands(char[][] grid) {
        int res = 0;
        ROW = grid.length;
        COL = grid[0].length;

        for(int i = 0; i < ROW; i++){
            for(int j = 0; j < COL; j++){
                if(grid[i][j] == '1'){
                    res++;
                    bfs(i, j, grid);
                }
            }
        }
        return res;
    }
}
