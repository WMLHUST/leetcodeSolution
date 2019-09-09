package main

import "fmt"

// 坐标转换公式 (x, y) -> (y, n-1-x)
// 公式思路，先做矩阵转置，再做对称
func rotate(matrix [][]int)  {
	loop := len(matrix) / 2
	n := len(matrix)

	for i:=0; i<loop; i++ {
		j := n - i
		for k := i; k<j-1; k++{
			curR := i
			curC := k
			nextVal := matrix[i][k]
			for q:=0; q<4; q++{
				nextR := curC
				nextC := n - 1 - curR
				tmp := matrix[nextR][nextC]
				matrix[nextR][nextC] = nextVal
				nextVal = tmp
				curR = nextR
				curC = nextC
			}
		}
	}

	return
}

func main() {
	arr := [][]int{
		{1,2,3},
		{4,5,6},
		{7,8,9},
	}

	rotate(arr)
	fmt.Println(arr)
}