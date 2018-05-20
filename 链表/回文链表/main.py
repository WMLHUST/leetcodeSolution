# coding: utf-8

from public_tools.List.LCList import LL

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        # 计算长度
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        # 找中间节点
        half_n = n // 2
        half_node = head
        for i in range(half_n):
            half_node = half_node.next

        head2 = self.reverseList(half_node)

        # 比较前n个节点
        for i in range(half_n):
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next

        return True

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
print(Solution().isPalindrome(ll.headNode))