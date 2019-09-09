class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cur = n
        tmp = []
        while cur>0:
            tmp.append(cur%10)
            cur = cur // 10
        next_n = 0
        for i in tmp:
            next_n += i**2

        if next_n == 1:
            return True
        elif next_n == 4:
            return False
        return self.isHappy(next_n)

print(Solution().isHappy(20))