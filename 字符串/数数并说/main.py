# coding: utf-8

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        x = '1'
        for i in range(1, n):
            strlen = len(x)
            i = 0
            next_x = ''
            while True:
                if not i<strlen:
                    break
                ch = x[i]
                j = i+1
                cnt = 1
                while True:
                    if j>=strlen or x[j]!=ch:
                        break
                    else:
                        cnt += 1
                        j += 1
                i = j
                next_x += str(cnt) + str(ch)
            x = next_x

        return x

print(Solution().countAndSay(7))
print(Solution().countAndSay(8))
print(Solution().countAndSay(9))
print(Solution().countAndSay(10))
print(Solution().countAndSay(30))