class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        res = float("inf")
        for i in range(len(coins)):
            c_i = len(coins)-1-i
            cur_cnt = amount // coins[c_i]
            cur = amount % coins[c_i]
            tmp = cur_cnt
            if cur == 0:
                res = min(tmp, res)

            for j in range(1, c_i+1):
                c_j = c_i - j
                cur_cnt = cur // coins[c_j]
                cur = cur % coins[c_j]
                tmp += cur_cnt
                if cur == 0:
                    res = min(tmp, res)
                    break
        return res

coins = [9, 5, 4, 1]
amount = 17
print(Solution().coinChange(coins, amount))