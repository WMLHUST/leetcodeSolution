# coding: utf-8

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # 每个节点都有最大值和最小值区间
        def isValid(root, min_val, max_val):

            if root is None:
                return True

            if root.val>=max_val or root.val<=min_val:
                return False

            return isValid(root.left, min_val, root.val) and isValid(root.right, root.val, max_val)

        return isValid(root, -pow(2, 31)-1, pow(2, 31))