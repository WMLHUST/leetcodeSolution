# coding: utf-8

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + (left_depth if left_depth>right_depth else right_depth)