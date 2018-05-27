# coding: utf-8

def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def isValid(node_left, node_right):
        if node_left==None and node_right==None:
            return True
        if (node_left==None) ^ (node_right==None) == True:
            return False

        return (node_left.val==node_right.val) and isValid(node_left.left, node_right.right) and \
                (isValid(node_left.right, node_right.left))

    if root is None:
        return True
    return isValid(root.left, root.right)
