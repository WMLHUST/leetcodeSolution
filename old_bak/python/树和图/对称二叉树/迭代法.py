# coding: utf-8

def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def isValid(nodes):
        n = len(nodes)
        for i in range(0, n//2):
            j = n-1-i
            if (nodes[i] is None) ^ (nodes[j] is None) == True:
                return False

            if nodes[i] is None and nodes[j] is None:
                continue

            if nodes[i].val != nodes[j].val:
                return False

        return True

    if root is None:
        return True
    nodes = [root]
    while True:
        if len(nodes) == 0:
            break
        if not isValid(nodes):
            return False
        tmp = []
        for i in nodes:
            if i is not None:
                tmp.append(i.left)
                tmp.append(i.right)
        nodes = tmp
    return True
