# coding: utf-8

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # 每个节点都有最大值和最小值区间
        def isValid(root, min_val, max_val):
            pass
 
        return isValid(root, -pow(2, 31)-1, pow(2, 31))