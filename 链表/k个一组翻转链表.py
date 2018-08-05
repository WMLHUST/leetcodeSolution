# coding: utf-8

# 被这道题的细节搞得神烦
# 关键在于1.计数；2.不能完全按照链表倒序的思想。
# 参考：https://blog.csdn.net/qq_17550379/article/details/80696835

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        h = ListNode(-1)
        h.next = head
        pre = h
        cur = head

        while cur != None:
            t = cur
            count = 1
            while count < k and t != None:
                t = t.next
                count += 1
            if count == k and t != None:
                # pre是前一个段的尾节点，倒序过程中位置不变，这个关键
                for _ in range(k - 1):
                    lat = cur.next
                    cur.next = lat.next
                    lat.next = pre.next
                    pre.next = lat

                pre = cur
                cur = pre.next
            else:
                break

        return h.next



