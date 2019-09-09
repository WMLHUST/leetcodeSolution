# coding: utf-8

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0

        curMin = 0
        curMax = 0
        TotalEarn = 0
        curEarn = 0
        for i in range(1, len(prices)):
            if prices[i]>prices[curMax]:
                curMax = i
                curEarn = prices[curMax]-prices[curMin]
            else:
                curMin = i
                curMax = i
                TotalEarn += curEarn
                curEarn = 0

        return TotalEarn+curEarn

if __name__=='__main__':
    s = Solution()
    res = s.maxProfit([7,1,5,3,6,4])
    print(res)
