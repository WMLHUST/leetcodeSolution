package main

import "fmt"

func maxProfit(prices []int) int {
	sum := 0
	for i:=1; i<len(prices); i++ {
		if prices[i] - prices[i-1] > 0 {
			sum += prices[i] - prices[i-1]
		}

	}

	return sum
}

func main() {
	prices := []int{7,1,5,3,6,4}
	fmt.Println(maxProfit(prices))
}