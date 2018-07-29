# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        cnt = 0
        # 由于python自动支持大数（其实是C语言的long型），所以只看低32位
        while (n&(2**32-1))!=0:
            n = n & (n-1)
            cnt += 1
        return cnt

print(Solution().NumberOf1(-1))