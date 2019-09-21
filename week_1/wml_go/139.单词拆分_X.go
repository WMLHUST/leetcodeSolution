/*
 * @lc app=leetcode.cn id=139 lang=golang
 *
 * [139] 单词拆分
 *
 * https://leetcode-cn.com/problems/word-break/description/
 *
 * algorithms
 * Medium (42.80%)
 * Likes:    196
 * Dislikes: 0
 * Total Accepted:    19K
 * Total Submissions: 44.4K
 * Testcase Example:  '"leetcode"\n["leet","code"]'
 *
 * 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
 *
 * 说明：
 *
 *
 * 拆分时可以重复使用字典中的单词。
 * 你可以假设字典中没有重复的单词。
 *
 *
 * 示例 1：
 *
 * 输入: s = "leetcode", wordDict = ["leet", "code"]
 * 输出: true
 * 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
 *
 *
 * 示例 2：
 *
 * 输入: s = "applepenapple", wordDict = ["apple", "pen"]
 * 输出: true
 * 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
 * 注意你可以重复使用字典中的单词。
 *
 *
 * 示例 3：
 *
 * 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
 * 输出: false
 *
 *
 */
func wordBreak(s string, wordDict []string) bool {
	ws := map[string]bool{}
	for _, v := range wordDict {
		ws[v] = true
	}

	dp := make([]int, len(s))
	if ws[s[0:1]] {
		dp[0] = 1
	}

	for i := 1; i < len(s); i++ {
		if ws[s[:i+1]] {
			dp[i] = 1
			continue
		}
		for j := 0; j < i; j++ {
			if dp[j] == 1 && ws[s[j+1:i+1]] {
				dp[i] = 1
				break
			}
		}
	}

	return dp[len(s)-1] == 1
}
