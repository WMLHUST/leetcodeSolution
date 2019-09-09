package main

import "fmt"

func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	cur := 0
	for i := 1; i < len(nums); i++{
		if nums[i] != nums[cur] {
			cur++
			nums[cur] = nums[i]
		}
	}

	return cur+1
}

func main() {
	nums := []int{0,0,1,1,1,2,2,3,3,4}
	removeDuplicates(nums)
	fmt.Println(nums)
}