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

        res_left = self.inorderTraversal(root.left)
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

            # 此时到了此循环开始时，cur节点的最左子节点
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

    def inorderTraversal3(self, root):
        stack = []
        cur = root
        res = []
        while cur!=None:
            while cur!=None:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res








