# -*- coding:utf-8 -*-
# 仔细体会F(N) 和 F(N-1) F(N-2)的关系。还是斐波那契
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2

        pre = 1
        cur = 2
        res = 0
        while number > 2:
            res = pre + cur
            pre = cur
            cur = res
            number -= 1
        return res