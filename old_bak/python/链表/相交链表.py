# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB==None:
            return None

        n1 = 0
        h1 = headA
        while h1!=None:
            n1+=1
            h1 = h1.next

        h2 = headB
        n2 = 0
        while h2!=None:
            n2 += 1
            h2 = h2.next

        isALong = True
        if n1<n2:
            isALong = False

        h1 = headA
        h2 = headB
        cnt_gap = abs(n1-n2)
        if isALong:
            while cnt_gap>0:
                h1 = h1.next
                cnt_gap -= 1
        else:
            while cnt_gap>0:
                h2 = h2.next
                cnt_gap -= 1
        while h1!=None and h2!=None:
            if h1==h2:
                return h1
            h1 = h1.next
            h2 = h2.next
        return None

# 奇人技巧啊。。当假设p1是短链，p1走完时，将p1指向长链头结点，此时p2距离尾节点l2-l1步。
# 之后当p2走到尾节点时，将p2指向短链，此时p1在长链走了l2-l1步，所以接下来p2和p1会重合。
# 原理一样，但是代码真的简洁。。。如果两个链表没有相交的节点，p1,p2会同时等于None，因此也会跳出循环，返回None
def getIntersectionNode2(self, headA, headB):
    p1 = headA
    p2 = headB
    while p1!=p2:
        p1 = headB if p1 == None else p1.next
        p2 = headA if p2 == None else p2.next

    return p1
