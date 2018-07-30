# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from public_tools.Tree.Tree import TreeNode

# 分治法，时间复杂度 n*log(n)*l，（要合并log(n)次，每层递归一共都是n*l个节点数，所以要n*l次，但是有log(n)层递归，所以一共n*l*log(n)）
# 如果直接遍历比较节点值，时间复杂度，n*l*n，（n*l总节点数，每取一个最小节点，要比较n次）
# n:链表个数，l链表平均长度
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeFunc(lists, l, r):
            if l==r:
                return lists[l]

            middle = (l + r) // 2
            lres = mergeFunc(lists, l, middle)
            rres = mergeFunc(lists, middle+1, r)

            cur = ListNode(0)
            head_ori = cur
            while lres!=None and rres!=None:
                if lres.val < rres.val:
                    cur.next = lres
                    lres = lres.next
                else:
                    cur.next = rres
                    rres = rres.next
                cur = cur.next

            if lres!=None:
                cur.next = lres
            elif rres!=None:
                cur.next = rres

            return head_ori.next

        if lists==None or len(lists)==0:
            return None
        return mergeFunc(lists, 0, len(lists)-1)
