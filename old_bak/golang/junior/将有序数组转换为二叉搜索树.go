package main

func sortedArrayToBST(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}

	if len(nums) == 1 {
		return &TreeNode{
			Val: nums[0],
		}
	}

	centre := len(nums) / 2
	root := &TreeNode{
		Val: nums[centre],
	}

	root.Left = sortedArrayToBST(nums[0:centre])
	root.Right = sortedArrayToBST(nums[centre+1:])

	return root
}
