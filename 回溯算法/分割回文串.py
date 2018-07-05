class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # 相当于dfs遍历，栈里保存的是结果
        def doPartition(s, stack, res):
            if len(s)==0:
                res.append(stack[:])
                return
            elif len(s) == 1:
                stack.append(s)
                res.append(stack[:])
                stack.pop()
                return

            for i in range(1, len(s)+1):
                if self.isPalind(s[:i]):
                    stack.append(s[:i])
                    doPartition(s[i:], stack, res)
                    stack.pop()

        if len(s)==0:
            return []

        stack = []
        res = []
        doPartition(s, stack, res)
        return res

    def isPalind(self, s):
        i = 0
        j = len(s) - 1
        while i<j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True


s = "aab"
print(Solution().partition(s))