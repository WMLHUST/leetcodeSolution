class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        bit_time = 1
        res = 0
        for i in range(n):
            # 倒序遍历
            j = n-1-i
            res += (ord(s[j]) - ord('A') + 1) * bit_time
            bit_time *= 26

        return res

print(Solution().titleToNumber("ZY"))