class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2

        import math
        dp = [n] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        # 总是超出时间限制，但是对于dp方法，n*sqrt(n)是最佳的时间复杂度了
        # 要不就用数学方法
        for i in range(3, n+1):
            for j in range(1, int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i-j*j] + 1)
        return dp[n]

n = 8285
print(Solution().numSquares(n))