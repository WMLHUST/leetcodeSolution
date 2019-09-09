package main

func longestPalindrome(s string) string {
	if len(s) == 0 {
		return ""
	}

	if len(s) == 1 {
		return s
	}

	l := len(s)
	dp := [l][l]int{}

	for i := 0; i < l; i++ {
		dp[i][i] = 1
	}

	for i := 0; i < l; i++ {
		for j := i + 1; j < l; j++ {
			if dp[i+1]
		}
	}
}
