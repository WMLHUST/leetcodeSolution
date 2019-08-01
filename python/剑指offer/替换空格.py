# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        space_cnt = 0
        for ch in s:
            if ch == ' ':
                space_cnt += 1

        res = [' '] * (len(s) + space_cnt * 2)
        cur = len(s) + space_cnt * 2 - 1
        for ch in s[::-1]:
            if ch == ' ':
                res[cur] = '0'
                res[cur - 1] = '2'
                res[cur - 2] = '%'
                cur = cur - 3
            else:
                res[cur] = ch
                cur = cur - 1
        print(''.join(res))


s = "we are happy"
print(Solution().replaceSpace(s))