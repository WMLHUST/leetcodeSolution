# coding: utf-8

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isLeft(c):
            return c=='(' or c=='{' or c=='['

        def isPair(c1, c2):
            return (c1=='(' and c2==')') or (c1=='{' and c2=='}') or (c1=='[' and c2==']')

        c_stack = []
        for c in s:
            if isLeft(c):
                # 左括号
                c_stack.append(c)
            else:
                # 右括号，抵消栈顶
                if len(c_stack)==0:
                    return False
                tmp = c_stack.pop()
                if not isPair(tmp, c):
                    return False

        return len(c_stack)==0

s = "{[]}"
print(Solution().isValid(s))