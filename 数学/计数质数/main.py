# coding: utf-8

import math

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        cache = [True] * n
        cache[0] = False
        cache[1] = False
        for i in range(2, n):
            if cache[i] == True:
                cache[i+i:n:i] = [False] * len(cache[i+i:n:i])
        return sum(cache)

print(Solution().countPrimes(499979))


