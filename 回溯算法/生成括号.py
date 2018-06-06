class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []

        res = []

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




