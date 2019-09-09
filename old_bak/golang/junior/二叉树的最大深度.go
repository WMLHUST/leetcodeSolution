package main

type TreeNode struct{
	Val int
	Left *TreeNode
	Right *TreeNode
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	lD := maxDepth(root.Left)
	rD := maxDepth(root.Right)

	var max = lD
	if rD > lD {
		max = rD
	}

	return max + 1
}