package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}

	res := [][]int{}
	ups := []*TreeNode{root}

	for ; len(ups)!=0; {
		nextUps := []*TreeNode{}
		curVals := []int{}
		for _, v:= range ups {
			if v == nil {
				continue
			}
			curVals = append(curVals, v.Val)
			if v.Left != nil {
				nextUps = append(nextUps, v.Left)
			}
			if v.Right != nil {
				nextUps = append(nextUps, v.Right)
			}
		}
		ups = nextUps
		res = append(res, curVals)
	}

	return res
}