# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from public_tools.Tree.Tree import TreeNode

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return []

        res = [root.val]
        level_stack = [root]
        while len(level_stack)>0:
            tmp_stack = []
            for item in level_stack:
                if item.left == None:
                    res.append(None)
                else:
                    res.append(item.left.val)
                    tmp_stack.append(item.left)

                if item.right == None:
                    res.append(None)
                else:
                    res.append(item.right.val)
                    tmp_stack.append(item.right)
            level_stack = tmp_stack

        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        root = TreeNode(data[0])
        level_stack = [root]
        i = 1
        while i<len(data):
            tmp_stack = []
            for node in level_stack:
                if i>len(data)-1:
                    return root
                if data[i] != None:
                    node.left = TreeNode(data[i])
                    tmp_stack.append(node.left)
                i += 1

                if i>len(data)-1:
                    return root
                if data[i] != None:
                    node.right = TreeNode(data[i])
                    tmp_stack.append(node.right)
                i += 1
            level_stack = tmp_stack

        return root

data = [1,2,3,None,None,4,5]


