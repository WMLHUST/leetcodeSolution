# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getDeepth(self, root):
        if root == None:
            return 0

        left_deepth = self.getDeepth(root.left)
        if left_deepth == -1:
            return -1

        right_deepth = self.getDeepth(root.right)
        if right_deepth == -1:
            return -1

        if abs(left_deepth-right_deepth)>1:
            return -1
        else:
            return max(left_deepth, right_deepth) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.getDeepth(root) == -1:
            return False

        return True

