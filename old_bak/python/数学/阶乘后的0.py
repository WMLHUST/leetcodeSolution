class Solution(object):
    # 因式分解，有多少个5，就有多少个0
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n>0:
            n = n//5
            res += n
        return res
