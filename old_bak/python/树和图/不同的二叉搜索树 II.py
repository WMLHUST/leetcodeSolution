# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 这个题写的还不对。。。。
class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def func(a):
            if len(a) == 0:
                return [[None]]

            if len(a) == 1:
                return [[TreeNode(a[0]).val]]

            res = []
            for i in range(len(a)):
                left = func(a[0:i])
                root = [TreeNode(a[i]).val]
                right = func(a[i + 1:])
                for left_item in left:
                    for right_item in right:
                        # 左子树比较长，右子树为空，则把右边插入左边第二个。。
                        if right_item == [None] and len(left_item)>1:
                            left_item.insert(1, None)
                        if right_item == [None]:
                            right_item = []

                        # 不应该这样，因为左子树为长序列，右子树也为长序列的时候（长序列：树深>2），不能这么相加，因为是层次遍历
                        res.append(root + left_item + right_item)

            return res

        a = [i for i in range(1, n+1)]
        res = func(a)
        return res

print(Solution().generateTrees(2))
