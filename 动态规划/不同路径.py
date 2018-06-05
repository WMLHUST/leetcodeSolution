class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [[0]*n for i in range(m)]
        res[0][0] = 1

        #计算第一行
        for j in range(n):
            res[0][j] = 1

        # 计算第一列
        for i in range(1, m):
            res[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = res[i-1][j] + res[i][j-1]

        return res[m-1][n-1]

print(Solution().uniquePaths(7, 3))
