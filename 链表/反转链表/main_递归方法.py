# coding: utf-8
import sys
sys.path.append(r"..\..\public_tools")

from public_tools.List.LCList import *

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next is None:
            return head

        cur = head
        third = cur.next.next
        cur.next.next = cur
        res = self.reverseList(cur.ne)

        return res

ll = LL([1, 2, 3])
Solution().reverseList(ll.headNode).printAfter()