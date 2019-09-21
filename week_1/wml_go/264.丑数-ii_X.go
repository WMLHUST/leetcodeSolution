/*
 * @lc app=leetcode.cn id=264 lang=golang
 *
 * [264] 丑数 II
 *
 * https://leetcode-cn.com/problems/ugly-number-ii/description/
 *
 * algorithms
 * Medium (47.26%)
 * Likes:    133
 * Dislikes: 0
 * Total Accepted:    8.7K
 * Total Submissions: 18.5K
 * Testcase Example:  '10'
 *
 * 编写一个程序，找出第 n 个丑数。
 *
 * 丑数就是只包含质因数 2, 3, 5 的正整数。
 *
 * 示例:
 *
 * 输入: n = 10
 * 输出: 12
 * 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
 *
 * 说明:
 *
 *
 * 1 是丑数。
 * n 不超过1690。
 *
 *
 */

// 思路：https://blog.csdn.net/guoziqing506/article/details/52347140

func nthUglyNumber(n int) int {
	uglyNums := []int{1}

	var i5 int = 0
	var min2, min3, min5 int
	for len(uglyNums) < n {
		var done2, done3, done5 bool

		last := uglyNums[len(uglyNums)-1]
		for i := i5; i < len(uglyNums); i++ {
			v := uglyNums[i]
			if !done2 {
				min2 = 2 * v
				if min2 > last {
					done2 = true
				}
			}

			if !done3 {
				min3 = 3 * v
				if min3 > last {
					done3 = true
				}
			}

			if !done5 {
				min5 = 5 * v
				if min5 > last {
					done5 = true
					// 避免每次从 i=0 开始计算，占用耗时
					i5 = i
				}
			}
		}

		min := min2
		if min3 < min {
			min = min3
		}
		if min5 < min {
			min = min5
		}
		uglyNums = append(uglyNums, min)
	}

	// fmt.Println(uglyNums)

	return uglyNums[n-1]
}
