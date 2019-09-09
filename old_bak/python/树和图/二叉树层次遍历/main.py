# coding: utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        res = []
        nodes = [root]
        while len(nodes)>0:
            next_nodes = []
            tmp = []
            for node in nodes:
                tmp.append(node.val)
                if node.left is not None:
                    next_nodes.append(node.left)
                if node.right is not None:
                    next_nodes.append(node.right)
            res.append(tmp)
            nodes = next_nodes
        return res