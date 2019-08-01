class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for i in range(0, amount+1):
            for j in coins:
                if j > i:
                    continue
                else:
                    dp[i] = min(dp[i], dp[i-j]+1)
        return dp[amount] if dp[amount] < float('inf') else -1


coins = [9, 5]
amount = 17
print(Solution().coinChange(coins, amount))