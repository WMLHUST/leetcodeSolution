# coding: utf-8
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2
        first = 1
        second = 2
        for i in range(2, n):
            next = first + second
            first, second = second, next

        return second

print(Solution().climbStairs(3))