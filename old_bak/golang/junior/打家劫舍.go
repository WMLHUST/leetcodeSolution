package main

import "fmt"

func rob(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	if len(nums) == 1 {
		return nums[0]
	}

	if len(nums) == 2 {
		if nums[0] > nums[1] {
			return nums[0]
		} else {
			return nums[1]
		}
	}

	last2 := nums[0]
	last1 := nums[1]
	if last1 < last2 {
		last1 = last2
	}

	for i := 2; i < len(nums); i++ {
		cur := nums[i] + last2

		last2 = last1
		if cur > last1 {
			last1 = cur
		}
	}

	if last1 > last2 {
		return last1
	} else {
		return last2
	}
}

func main() {
	fmt.Println(rob([]int{1, 2, 3, 1}))
}
