class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_cnt = len(grid)
        col_cnt = len(grid[0])
        dp = [[0]*col_cnt for _ in range(row_cnt)]
        dp[0][0] = grid[0][0]

        for i in range(1, row_cnt):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(1, col_cnt):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, row_cnt):
            for j in range(1, col_cnt):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[row_cnt-1][col_cnt-1]

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(Solution().minPathSum(grid))