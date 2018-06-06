class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row_n = len(grid)
        if row_n == 0:
            return 0
        col_n = len(grid[0])

        def mark_zero(grid, i, j):
            if i - 1 >=0 and grid[i-1][j] == '1':
                grid[i-1][j] = 0
                mark_zero(grid, i-1, j)

            if i+1 < row_n and grid[i+1][j] == '1':
                grid[i+1][j] = 0
                mark_zero(grid, i+1, j)

            if j-1>=0 and grid[i][j-1] == '1':
                grid[i][j-1] = 0
                mark_zero(grid, i, j-1)

            if j+1 < col_n and grid[i][j+1] == '1':
                grid[i][j+1] = 0
                mark_zero(grid, i, j+1)

        res = 0
        for i in range(row_n):
            for j in range(col_n):
                if grid[i][j] == '1':
                    res += 1
                    grid[i][j] = 0
                    mark_zero(grid, i, j)

        return res

grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]

grid = [["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]]
print(Solution().numIslands(grid))