# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from public_tools.Tree.Tree import Tree

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res_max = root.val
        def getSum(root):
            left_res = None
            if root.left != None:
                left_res = getSum(root.left)
                self.res_max = max(left_res, self.res_max)
            else:
                left_res = 0

            right_res = None
            if root.right != None:
                right_res = getSum(root.right)
                self.res_max = max(right_res, self.res_max)
            else:
                right_res = 0

            res = max(root.val, root.val+left_res, root.val+right_res)

            # 算最终结果时，多一种情况，即root节点连通左右子树的情况
            self.res_max = max(res, self.res_max, root.val+left_res+right_res)
            return res

        getSum(root)
        return self.res_max

data = [1,2,3]
data = [-10,9,20,None,None,15,7]
# data = [5,4,8,11,None,13,4,7,2,None,None,None,1]
tree = Tree(data)
print(Solution().maxPathSum(tree.root))
