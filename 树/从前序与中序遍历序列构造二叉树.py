# coding: utf-8

from public_tools.Tree.Tree import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        p_n = len(preorder)
        if p_n == 0:
            return None

        if p_n == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        in_index = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:in_index+1], inorder[0:in_index])
        root.right = self.buildTree(preorder[in_index+1:], inorder[in_index+1:])
        return root