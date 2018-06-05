# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return

        level_stack = [root]
        while len(level_stack)>0:
            n = len(level_stack)

            tmp = []
            for i in range(n-1):
                if level_stack[i].left != None:
                    tmp.append(level_stack[i].left)
                if level_stack[i].right != None:
                    tmp.append(level_stack[i].right)
                level_stack[i].next = level_stack[i+1]

            level_stack[n - 1].next = None
            if level_stack[n-1].left != None:
                tmp.append(level_stack[n-1].left)
            if level_stack[n-1].right != None:
                tmp.append(level_stack[n-1].right)

            level_stack = tmp