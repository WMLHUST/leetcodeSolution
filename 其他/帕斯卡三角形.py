# coding: utf-8

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows == 0:
            return res

        res.append([1])
        if numRows == 1:
            return res

        res.append([1, 1])
        if numRows == 2:
            return res


        for i in range(2, numRows):
            pre_level_len = len(res[i-1])
            tmp = []
            for j in range(0, i+1):
                if j == 0:
                    # 第一个
                    tmp.append(1)
                elif j == i:
                    # 最后一个
                    tmp.append(1)
                    break
                else:
                    tmp.append(res[i-1][j-1] + res[i-1][j])
            res.append(tmp)
        return res

print(Solution().generate(5))