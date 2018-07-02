# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root == None:
            return []

        res = []
        level_stack = [root]
        level_cnt = 0
        while len(level_stack)>0:
            tmp = []
            tmp_res = []
            for i in range(len(level_stack)):
                j = i if level_cnt % 2 == 0 else len(level_stack)-1-i
                tmp_res.append(level_stack[j].val)

                if level_stack[i].left != None:
                    tmp.append(level_stack[i].left)
                if level_stack[i].right != None:
                    tmp.append(level_stack[i].right)

            level_stack = tmp
            res.append(tmp_res)
            level_cnt += 1
        return res