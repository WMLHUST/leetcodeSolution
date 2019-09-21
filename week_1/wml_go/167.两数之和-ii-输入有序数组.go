/*
 * @lc app=leetcode.cn id=167 lang=golang
 *
 * [167] 两数之和 II - 输入有序数组
 */
func twoSum(numbers []int, target int) []int {
	i := 0
	j := len(numbers) - 1
	for {
		sum := numbers[i] + numbers[j]
		if sum == target {
			return []int{i+1, j+1}
		}
		if sum > target {
			j--
		} else if sum < target {
			i++
		}
	}
}
