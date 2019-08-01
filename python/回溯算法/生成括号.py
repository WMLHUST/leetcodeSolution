class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []

        res = []

        # 计算字符串左、右括号数量，如果左括号数量>右括号数量，就可以添加右括号，然后继续dfs
        # 如果左括号数量<总长度，就可以添加左括号，实际可以结合右括号数量进一步限制，即左括号-右括号数量 < 总长度-左括号-右括号
        def dfs(left_cnt, right_cnt, tmp_res):
            if left_cnt==n and right_cnt==n:
                res.append(tmp_res)

            if left_cnt < n:
                dfs(left_cnt+1, right_cnt, tmp_res+'(')

            if left_cnt > right_cnt:
                dfs(left_cnt, right_cnt+1, tmp_res+')')

        dfs(0, 0, "")
        return res

print(Solution().generateParenthesis(4))




