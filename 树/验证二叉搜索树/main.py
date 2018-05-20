# coding: utf-8

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSubTreeLessThan(root, val):
            if root is None:
                return True
            return root.val<val and isSubTreeLessThan(root.left, val) and isSubTreeLessThan(root.right, val)

        def isSubTreeGreaterThan(root, val):
            if root is None:
                return True
            return root.val>val and isSubTreeGreaterThan(root.left, val) and isSubTreeGreaterThan(root.right, val)


        if root is None:
            return True

        return self.isValidBST(root.left) and self.isValidBST(root.right) and isSubTreeGreaterThan(root.right, root.val) and isSubTreeLessThan(root.left, root.val)