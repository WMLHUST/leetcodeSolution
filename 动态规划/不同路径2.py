class Solution:
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m==0:
            return 0
        n = len(grid[0])

        dp = [[0] * n ]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                    continue

                if i==0 and j==0:
                    continue

                if i==0:
                    dp[0][j] = dp[0][j-1]
                    continue

                if j==0:
                    dp[i][0] = dp[i-1][0]
                    continue

                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

gird = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print(Solution().uniquePathsWithObstacles(gird))

