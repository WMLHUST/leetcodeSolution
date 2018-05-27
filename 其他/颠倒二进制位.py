# coding: utf-8

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        if n == 0:
            return 0

        nb = bin(n)[2:]
        if len(nb)<32:
            nb = '0'*(32-len(nb)) + nb[:]
        nb2 = nb[::-1]
        return int(nb2, 2)

    def reverseBits2(self, n):
        nb = bin(n)[:1:-1]
        nb2 = nb.ljust(32, '0')
        return int(nb2, 2)

n = 43261596
print(Solution().reverseBits2(n))