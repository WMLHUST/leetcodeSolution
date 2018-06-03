# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归
        if root is None:
            return []

        res_left = res_right = []
        if root.left != None:
            res_left = self.inorderTraversal(root.left)
        if root.right != None:
            res_right = self.inorderTraversal(root.right)

        return res_left + [root.val] + res_right

    # 迭代关键，遍历左节点后，pop中间节点，然后对右节点做同样操作
    def inorderTraversal2(self, root):
        if root is None:
            return []

        stack = []
        res = []
        cur = root
        while cur!=None or len(stack)>0:
            while cur != None:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res






