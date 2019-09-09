package main

func maxSubArray(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	res := nums[0]
	var max = res
	for i := 1; i < len(nums); i++ {
		tmp := res + nums[i]
		if tmp > nums[i] {
			res = tmp
		} else {
			res = nums[i]
		}

		if res > max {
			max = res
		}
	}

	return max
}
