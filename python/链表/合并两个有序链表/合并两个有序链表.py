# coding: utf-8

import sys
from public_tools.List import LCList

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        cur1 = l1
        cur2 = l2
        if l1.val < l2.val:
            head = l1
            cur1 = cur1.next
        else:
            head = l2
            cur2 = cur2.next

        cur = head

        while True:
            if cur1 is None:
                cur.next = cur2
                return head
            if cur2 is None:
                cur.next = cur1
                return head

            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 = cur1.next
                cur = cur.next
            else:
                cur.next = cur2
                cur2 = cur2.next
                cur = cur.next

l1 = LCList.LL([1, 2, 4])
l2 = LCList.LL([1, 3, 4])
Solution().mergeTwoLists(l1.headNode, l2.headNode).printAfter()