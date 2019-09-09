import copy
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        word_dict = {}
        for item in wordDict:
            word_dict[item] = 1

        res = [[] for _ in range(len(s)+1)]
        dp = [0] * (len(s)+1)
        dp[0] = 1

        for i in range(len(s)):
            for j in range(0, i+1):
                if dp[j]==1 and s[j:i+1] in word_dict:
                    dp[i+1] = 1
                    if len(res[j]) == 0:
                        res[i+1].append([s[j:i+1]])
                    else:
                        tmp = copy.deepcopy(res[j])
                        for item in tmp:
                            item.append(s[j:i+1])
                            res[i+1].append(item)

        res_tmp = []
        for item in res[i+1]:
            res_tmp.append(" ".join(item))
        return res_tmp

    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        Solution.res = []
        self.dfs(s, wordDict, '')
        return Solution.res

    def dfs(self, s, wordDict, stringlist):
        if self.check(s, wordDict):
            if len(s) == 0:
                Solution.res.append(stringlist[1:])
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    # print stringlist+' '+s[:i]
                    self.dfs(s[i:], wordDict, stringlist + ' ' + s[:i])

    def check(self, s, wordDict):
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if dp[j] and s[j:i + 1] in wordDict:
                    dp[i + 1] = True
                    break
        return dp[len(s)]

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]

print(Solution().wordBreak2(s, wordDict))