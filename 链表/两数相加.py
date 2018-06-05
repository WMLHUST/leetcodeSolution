# coding: utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from public_tools.List.LCList import ListNode
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c1 = l1
        c2 = l2
        res_head = ListNode(0)
        cur = res_head
        sum = ""

        carry = 0
        while c1!= None or c2!=None:
            tmp = 0
            if c1!=None:
                tmp += c1.val
                c1 = c1.next
            if c2!=None:
                tmp += c2.val
                c2 = c2.next
            tmp2 = tmp + carry
            cur.next = ListNode(tmp2%10)
            cur = cur.next
            carry = tmp2/10
        if carry>0:
            cur.next = ListNode(carry)

        return res_head.next
