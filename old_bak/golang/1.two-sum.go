/*
 * @lc app=leetcode id=1 lang=golang
 *
 * [1] Two Sum
 */
func twoSum(nums []int, target int) []int {
	var res = make([]int, 2)
    for i:=0; i<len(nums); i++ {
		for j:=i+1; j<len(nums); j++ {
			if nums[i] + nums[j] == target {
				res = []int{i, j}
			}
		}
	}

	return res
}

