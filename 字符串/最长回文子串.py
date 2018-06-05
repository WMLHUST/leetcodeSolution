class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0:
            return ""
        if n == 1:
            return s
        if n==2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        max_len = 0
        left = -1
        right = -1
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1):
            dp[i][i] = 1
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                max_len = 2
                left = i
                right = i+1
            else:
                dp[i][i+1] = 0
        dp[n-1][n-1] = 1


        for i in range(2, n):
            i = n-1-i
            for j in range(i+2, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                    if dp[i][j] == 1:
                        if j-i+1 > max_len:
                            max_len = j-i+1
                            left = i
                            right = j
                else:
                    dp[i][j] = 0

        if max_len == 0:
            return s[0]

        return s[left:right+1]

s = "babad"
print(Solution().longestPalindrome(s))

