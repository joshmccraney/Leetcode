class Solution:
    def minPathSum(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        
        # first row
        for i in range(1, cols):
            grid[0][i] += grid[0][i-1]
        
        # first col
        for i in range(1, rows):
            grid[i][0] += grid[i-1][0]

        # inner cells
        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] += min( grid[i-1][j], grid[i][j-1] )
        return grid[-1][-1]

if __name__ == "__main__":
    ob1 = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(ob1.minPathSum(grid))