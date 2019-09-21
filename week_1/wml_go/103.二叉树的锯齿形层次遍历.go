/*
 * @lc app=leetcode.cn id=103 lang=golang
 *
 * [103] 二叉树的锯齿形层次遍历
 *
 * https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/
 *
 * algorithms
 * Medium (51.58%)
 * Likes:    90
 * Dislikes: 0
 * Total Accepted:    17.7K
 * Total Submissions: 34.3K
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
 *
 * 例如：
 * 给定二叉树 [3,9,20,null,null,15,7],
 *
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 *
 *
 * 返回锯齿形层次遍历如下：
 *
 * [
 * ⁠ [3],
 * ⁠ [20,9],
 * ⁠ [15,7]
 * ]
 *
 *
 */
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func zigzagLevelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}

	var res = [][]int{}
	var level = []*TreeNode{root}

	var order int
	for ; len(level) > 0; order++ {
		var levelRes []int
		var nextLevel []*TreeNode

		for i := 0; i < len(level); i++ {
			// 节点保持顺序存储
			v := level[i]
			if v.Left != nil {
				nextLevel = append(nextLevel, v.Left)
			}
			if v.Right != nil {
				nextLevel = append(nextLevel, v.Right)
			}

			// 顺序，偶数顺序，奇数倒序
			if order%2 == 0 {
				levelRes = append(levelRes, v.Val)
			} else {
				levelRes = append(levelRes, level[len(level)-1-i].Val)
			}
		}

		res = append(res, levelRes)
		level = nextLevel
	}
	return res
}
