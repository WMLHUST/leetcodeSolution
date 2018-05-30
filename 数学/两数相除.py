# coding: utf-8

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        isNeg = False
        if (dividend<0 and divisor>0):
            isNeg = True
        elif (dividend>0 and divisor<0):
            isNeg = True
        dividend = abs(dividend)
        divisor = abs(divisor)

        res = 0
        tmp_d1 = dividend
        while tmp_d1>=divisor:

            i = 1
            tmp_d2 = divisor
            while tmp_d2 <= tmp_d1:
                i = i<<1
                tmp_d2 = tmp_d2 << 1
            res = res + (i>>1)

            tmp_d1 = tmp_d1 - (tmp_d2>>1)

        # if tmp_d1 == divisor:
        #     res += 1

        if isNeg:
            if res<=(2<<30):
                return -res
            else:
                return -((2<<30)-1)

        if res<=((2<<30)-1):
            return res
        else:
            return (2<<30)-1

print(Solution().divide(-2147483648, -1))