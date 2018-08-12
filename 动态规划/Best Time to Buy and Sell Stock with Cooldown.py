class Solution():
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n<2:
            return 0

        if n==2:
            return 0 if prices[0]>=prices[1] else prices[1]-prices[0]

        sell = [0] * n
        buy = [0] * n

        buy[0] = -prices[0]
        buy[1] = max(-prices[0], -prices[1])

        sell[1] = max(sell[0], buy[0] + prices[1])

        for i in range(2, n):
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])

        return sell[n-1]

    def maxProfit2(self, prices):
        n = len(prices)
        if n < 2:
            return 0

        if n == 2:
            return 0 if prices[0] >= prices[1] else prices[1] - prices[0]

        sell = [0] * n
        buy = [0] * n

        buy[0] = -prices[0]
        for i in range(1, n):
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            buy[i] = max(buy[i-1], (sell[i-2] if i>1 else 0) - prices[i])

        return sell[n-1]



prices = [6,1,3,2,4,7]
prices = [1,2,3,0,2]
print(Solution().maxProfit(prices))