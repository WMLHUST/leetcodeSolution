/*
 * @lc app=leetcode.cn id=144 lang=golang
 *
 * [144] 二叉树的前序遍历
 *
 * https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/
 *
 * algorithms
 * Medium (61.69%)
 * Likes:    145
 * Dislikes: 0
 * Total Accepted:    38.6K
 * Total Submissions: 62.6K
 * Testcase Example:  '[1,null,2,3]'
 *
 * 给定一个二叉树，返回它的 前序 遍历。
 *
 * 示例:
 *
 * 输入: [1,null,2,3]
 * ⁠  1
 * ⁠   \
 * ⁠    2
 * ⁠   /
 * ⁠  3
 *
 * 输出: [1,2,3]
 *
 *
 * 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
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

func preorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	stack := []*TreeNode{root}
	res := []int{}
	cur := root
	isEnd := false
	for !isEnd {
		if cur == nil {
			break
		}

		res = append(res, cur.Val)
		if cur.Left != nil {
			stack = append(stack, cur.Left)
			cur = cur.Left
			continue
		}

		// 往回找第一个有右子树的
		for {
			if len(stack) == 0 {
				isEnd = true
				break
			}

			cur = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if cur.Right != nil || len(stack) == 0 {
				cur = cur.Right
				stack = append(stack, cur)
				break
			}
		}
	}

	return res
}
