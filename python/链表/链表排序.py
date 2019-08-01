# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # 最好理解的链表排序办法了，每次从中间分开，对两半链表进行排序，然后再合并。
    # 总得来说，算是归并吧
    # 划分次数log(n)，平均比较次数n/2，所以时间复杂度 nlog(n)
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        tmp = slow.next
        slow.next = None

        head1 = self.sortList(head)
        head2 = self.sortList(tmp)

        return self.mergeSortList(head1, head2)

    def mergeSortList(self, head1, head2):
        if head1 == None:
            return head2
        if head2 == None:
            return head1

        new_head = ListNode(0)
        cur = new_head
        while(head1!=None and head2!=None):
            if head1.val<head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next

        if head1!=None:
            cur.next = head1
        if head2!=None:
            cur.next = head2

        return new_head.next
