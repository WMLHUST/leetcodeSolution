# coding: utf-8

import math

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 2:
            return 0

        res = 0
        for i in range(3, n):
            cnt = int(math.sqrt(i))
            is_prime = True
            for j in range(2, cnt+1):
                if i % j == 0:
                    is_prime = False
                    break

            if is_prime:
                res += 1

        return res + 1

print(Solution().countPrimes(10))
