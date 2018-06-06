class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i in ['+', '-', '*', '/']:
                n2 = stack.pop()
                n1 = stack.pop()
                tmp = int(eval("n1"+i+"n2"))
                stack.append(tmp)
            else:
                stack.append(int(i))

        return stack.pop()

print(Solution().evalRPN(["4", "13", "5", "/", "+"]))