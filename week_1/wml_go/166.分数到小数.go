import "fmt"

/*
 * @lc app=leetcode.cn id=166 lang=golang
 *
 * [166] 分数到小数
 *
 * https://leetcode-cn.com/problems/fraction-to-recurring-decimal/description/
 *
 * algorithms
 * Medium (24.76%)
 * Likes:    64
 * Dislikes: 0
 * Total Accepted:    5K
 * Total Submissions: 20.2K
 * Testcase Example:  '1\n2'
 *
 * 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。
 *
 * 如果小数部分为循环小数，则将循环的部分括在括号内。
 *
 * 示例 1:
 *
 * 输入: numerator = 1, denominator = 2
 * 输出: "0.5"
 *
 *
 * 示例 2:
 *
 * 输入: numerator = 2, denominator = 1
 * 输出: "2"
 *
 * 示例 3:
 *
 * 输入: numerator = 2, denominator = 3
 * 输出: "0.(6)"
 *
 *
 */
func fractionToDecimal(a int, b int) string {
	iN := a / b
	mod := a % b
	if mod == 0 {
		return fmt.Sprintf("%v", iN)
	}

	var isNeg bool
	if a < 0 && b > 0 {
		a = -a
		isNeg = true
		iN = -iN
		if mod < 0 {
			mod = -mod
		}
	}
	if a > 0 && b < 0 {
		b = -b
		isNeg = true
		iN = -iN
		if mod < 0 {
			mod = -mod
		}
	}

	var dNRes string
	var modMap = make(map[int]int)

	for i := 0; mod != 0; i++ {
		lastIndex, ok := modMap[mod]
		if ok {
			dNRes = dNRes[:lastIndex] + "(" + dNRes[lastIndex:] + ")"
			break
		} else {
			modMap[mod] = i
		}

		dN := mod * 10 / b
		dNRes = fmt.Sprintf("%v%v", dNRes, dN)

		newMod := (mod * 10) % b
		mod = newMod
	}
	if isNeg {
		return fmt.Sprintf("-%v.%v", iN, dNRes)
	} else {
		return fmt.Sprintf("%v.%v", iN, dNRes)
	}
}
