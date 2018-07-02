# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from public_tools.Tree.Tree import TreeNode

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(nums[0])
        root = TreeNode(nums[n//2])
        root.left = self.sortedArrayToBST(nums[0:n//2])
        root.right = self.sortedArrayToBST(nums[n//2+1:n])
        return root