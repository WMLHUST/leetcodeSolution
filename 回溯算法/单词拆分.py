class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_dict = {}
        for item in wordDict:
            word_dict[item] = 1

        dp = [0] * len(s)
        if s[0] in word_dict:
            dp[0] = 1

        for i in range(1, len(s)):
            if s[0:i+1] in word_dict:
                dp[i] = 1
                continue

            for j in range(0, i+1):
                if dp[j] == 1 and s[j+1:i+1] in word_dict:
                    dp[i] = 1
                    break

        return dp[len(s)-1]==1

    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_dict = {}
        for item in wordDict:
            word_dict[item] = 1

        dp = [0] * (len(s)+1)
        dp[0] = 1

        for i in range(0, len(s)):
            for j in range(0, i+1):
                if dp[j] == 1 and s[j:i + 1] in word_dict:
                    dp[i+1] = 1
                    break

        return dp[len(s)] == 1

s = "a"
wordDict = ["a"]
print(Solution().wordBreak2(s, wordDict))
