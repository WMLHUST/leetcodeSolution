# coding: utf-8

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0

        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            cur_profit = prices[i] - min_price
            if max_profit<cur_profit:
                max_profit = cur_profit

            if min_price>prices[i]:
                min_price = prices[i]

        return max_profit

prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))