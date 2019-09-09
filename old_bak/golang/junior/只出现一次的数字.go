package main

func singleNumber(nums []int) int {
	var res int
	for _, v:=range nums {
		res = res ^ v
	}

	return res
}