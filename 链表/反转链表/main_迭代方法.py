# coding: utf-8

import sys
sys.path.append(r"../../public_tools")
from public_tools.List.LCList import *

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        slow = head
        fast = head
        while fast.next:
            next = fast.next
            fast.next = slow
            slow = fast
            fast = next

        fast.next = slow
        head.next = None
        return fast

    def reverseList(self, head, k):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        slow = head
        fast = head
        cnt = 0
        while fast.next and cnt<=k-2:
            next = fast.next
            fast.next = slow
            slow = fast
            fast = next
            cnt += 1

        fast.next = slow
        head.next = None
        return fast

ll = LL([1, 2, 3, 4])
Solution().reverseList(ll.headNode, 2).printAfter()
