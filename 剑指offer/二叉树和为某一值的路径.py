# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from public_tools.Tree.Tree import Tree
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        def doSearch(root, stack, target, res, cur):
            if root.left == None and root.right == None:
                if (cur + root.val) == target:
                    res.append(stack + [root.val])
                else:
                    return

            stack.append(root.val)
            if root.left != None:
                doSearch(root.left, stack, target, res, cur + root.val)
            if root.right != None:
                doSearch(root.right, stack, target, res, cur + root.val)
            stack.pop()

        if root == None:
            return []

        stack = []
        res = []
        cur = 0
        doSearch(root, stack, expectNumber, res, cur)
        return res


tree = Tree([10, 5, 12, 4, 7, None, None])
print(Solution().FindPath(tree.root, 22))