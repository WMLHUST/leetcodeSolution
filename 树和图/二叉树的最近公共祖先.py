# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return None

        if root.val==p.val or root.val==q.val:
            return root

        l_res = self.lowestCommonAncestor(root.left, p, q)
        r_res = self.lowestCommonAncestor(root.right, p, q)

        if l_res!=None and r_res!=None:
            return root

        if l_res!=None:
            return l_res
        if r_res!=None:
            return r_res