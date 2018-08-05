# coding: utf-8


# 维护三个指针，每次往后移动，交换两个
# p2/p3是待交换的两个节点，p1把它们前面的节点保存下来。
# head_tmp是辅助节点
class Solution():
    def swapPairs(self, head):
        if head==None or head.next == None:
            return head

        head_tmp = ListNode(0)
        p1 = head_tmp
        p2 = head
        p3 = head.next

        while p1!=None and p2!=None and p3!=None:
            p2.next = p3.next
            p3.next = p2
            p1.next = p3

            p1 = p2
            p2 = p2.next
            p3 = p2.next if p2!=None else None

        return head_tmp.next