# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inOrder(root):
            if root == None:
                return []

            left_res = inOrder(root.left)
            right_res = inOrder(root.right)
            return left_res + [root.val] + right_res

        res = inOrder(root)
        return res[k-1]