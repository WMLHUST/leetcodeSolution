# coding: utf-8

# 每条竖边和一条斜边作为一个基本单位
# 斜边和竖边上的索引相隔位置是固定的

class Solution:
    def convert(self, s, n):
        if n==0:
            return s

        cols = len(s) // (2*n-2)

        res = ""

        for i in range(0, n):
            for j in range(0, cols+1):
                # 这是竖条上的
                index = j * (2 * n - 2) + i
                if index > len(s) - 1:
                    break
                res += s[index]

                if i != 0 and i!=n-1:
                    # 斜边上的每个再加1个字母，
                    # 斜边索引 = 竖边索引 + 当前行和最后一行相差行数 * 2
                    index += (n-i-1) * 2
                    if index > len(s) - 1:
                        break
                    res += s[index]

        return res

s = "PAYPALISHIRING"
n = 4
print(Solution().convert(s, n))






