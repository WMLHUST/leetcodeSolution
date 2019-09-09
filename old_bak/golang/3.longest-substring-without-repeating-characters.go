package main

import "fmt"

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
	for i:=0; i<len(seen); i++{
		seen[i] = -1
	}

	start := 0
	res := 1
	seen[s[0]] = 0

	for i:=1; i<len(s); i++ {
		var index uint8 = s[i]

		if seen[index] >=0 {
			if seen[index] >= start {
				if res < i-start {
					res = i-start
				}

				start = seen[index] + 1
			}
		}

		seen[index] = i
	}

	if len(s) - start > res {
		res = len(s) - start
	}

	return res
}

func main() {
	str := "cdd"
	if lengthOfLongestSubstring(str) != 2 {
		fmt.Println(str, lengthOfLongestSubstring(str))
	}

	str2 := "abc"
	if lengthOfLongestSubstring(str2) != 3 {
		fmt.Println(str2, lengthOfLongestSubstring(str2))
	}

	str3 := "abcabcbb"
	if lengthOfLongestSubstring(str3) != 3 {
		fmt.Println(str3, lengthOfLongestSubstring(str3))
	}
}

