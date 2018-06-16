# coding: utf-8

class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree():
    def __init__(self, data):
        self.root = self.buildTree(data)

    def buildTree(self, data):
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