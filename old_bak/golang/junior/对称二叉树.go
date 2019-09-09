package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}

	return valid(root.Left, root.Right)
}

func valid(left *TreeNode, right *TreeNode) bool{
	if left == nil && right == nil {
		return true
	}

	if left == nil  && right != nil {
		return false
	}

	if left != nil && right == nil {
		return false
	}

	if left.Val != right.Val {
		return false
	}

	return valid(left.Left, right.Right) && valid(left.Right, right.Left)
}