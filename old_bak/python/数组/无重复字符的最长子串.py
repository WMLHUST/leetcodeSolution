# coding: utf-8

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 保存最近的字符索引
        cache = {}
        i = 0
        max_len = 0
        curstart = 0
        while i<len(s):
            if s[i] in cache.keys() and cache[s[i]]>=curstart:
                # ch 出现过，起点更新为ch原位置的下一个
                curstart = cache[s[i]] + 1
                cache[s[i]] = i
                i += 1
                continue
            else:
                # ch没出现过
                tmp_len = i - curstart + 1
                max_len = max(max_len, tmp_len)
                cache[s[i]] = i
                i += 1
        tmp_len = len(s)-curstart
        max_len = max(max_len, tmp_len)
        return max_len

s = "bbbbbb"
print(Solution().lengthOfLongestSubstring(s))
