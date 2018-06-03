# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        l1 = head
        l2 = head.next
        cur1 = l1
        cur2 = l2

        while cur1.next != None or cur2.next != None:
            cur1.next = cur2.next
            cur1 = cur2.next
            cur2.next = cur2.next.next
            cur2 = cur2.next.next

        cur1.next = l2
        return l1

