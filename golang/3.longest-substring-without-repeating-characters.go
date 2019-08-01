/*
 * @lc app=leetcode id=3 lang=golang
 *
 * [3] Longest Substring Without Repeating Characters
 */
func lengthOfLongestSubstring(s string) int {
	if len(s) == 0 {
		return 0
	}

	seen := make([]int, 128)
	// for i:=0; i<len(seen); i++{
	// 	seen[i] = -1
	// }

	start := 0
	res := 1
	seen[s[0] - ' '] = 1
	
	var ord int
	for i:=1; i<len(s); i++ {
		ord = int(s[i] - ' ')
		
		if seen[ord] >= start + 1{
			// seen
			start = seen[ord] // new start

		} else {
			if i - start > res {
				res = i - start + 1
			}
		}
		seen[ord] = i+1
	}

	if len(s) - start > res {
		res = len(s) - start
	}

	return res
} 

