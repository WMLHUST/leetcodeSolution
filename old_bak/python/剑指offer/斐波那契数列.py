# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        pre = 0
        cur = 1
        res = 0
        while n > 1:
            res = pre + cur
            pre = cur
            cur = res
            n -= 1
        return res
