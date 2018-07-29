# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        cur_out = 0
        for item in pushV:
            if popV[cur_out] == item:
                cur_out += 1
                continue
            else:
                stack.append(item)

        for i in range(cur_out, len(popV)):
            if popV[i] == stack[-1]:
                stack.pop()
            else:
                return False

        return True


pushV = [1, 2, 3, 4, 5]
popV = [4, 5, 3, 2, 1]
print(Solution().IsPopOrder(pushV, popV))