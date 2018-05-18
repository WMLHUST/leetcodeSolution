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

ll = LL([1])
Solution().reverseList(ll.headNode).printAfter()
