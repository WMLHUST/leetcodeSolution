package main

import "fmt"

func subsets(nums []int) [][]int {
	l := len(nums)
	if l == 1 {
		return [][]int{
			{},
			{nums[0]},
		}
	}

	subs := subsets(nums[1:])
	res := [][]int{}
	for _, v := range subs {
		nv := append(v, nums[0])

		res = append(res, append(v, nums[0]))
		res = append(res, v)
	}

	return res
}

func main() {
	nums := []int{1, 2, 3, 4, 5}
	fmt.Println("len: %v\n", len(subsets(nums)))
	fmt.Println(subsets(nums))
}
