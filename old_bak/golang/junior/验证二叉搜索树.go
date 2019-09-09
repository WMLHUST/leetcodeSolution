package main

func isValidBST(root *TreeNode) bool {
	return valid(root, MIN_INF, MAX_INF)
}

const MIN_INF = -(2<<31)
const MAX_INF = 2<<31

func valid(root *TreeNode, min int, max int) bool {
	if root == nil {
		return true
	}

	if root.Val >= max || root.Val <= min {
		return false
	}

	lValid := valid(root.Left, min, root.Val)
	rValid := valid(root.Right, root.Val, max)

	return lValid && rValid
}