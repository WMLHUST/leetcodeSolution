# -*- coding:utf-8 -*-

# 每次跳台阶和前面所有步骤有关
# F(n) = F(1) + F(2) + ... + F(n-1) + 1，最后的加1是因为，可能会一步跳到N
class Solution:
    def jumpFloorII(self, number):
        # write code here
        dp = [0] * number
        dp[0] = 1
        for i in range(1, number):
            dp[i] = 1
            for j in range(0, i):
                dp[i] += dp[j]

        return dp[number - 1]