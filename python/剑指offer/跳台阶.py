# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
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