# python由于 不限制32位，所以对于负数无法处理。。。。。

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # if (a <0 and b>0):


        xor = a ^ b
        bit_and = (a & b)<<1

        while bit_and!=0:
            tmp = xor
            xor = xor ^ bit_and
            print(tmp, xor)
            bit_and = (tmp & bit_and)<<1

        return xor
a = -2
print(Solution().getSum(a, 7))
