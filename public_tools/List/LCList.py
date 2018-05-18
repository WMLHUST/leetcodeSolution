# coding: utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printAfter(self):
        print(self.val, end='')
        next = self.next
        while next:
            print(',', next.val, end='')
            next = next.next

class LL:
    def __init__(self, vals):
        head = None
        cur = None

        for i in vals:
            node = ListNode(i)
            if head is None:
                head = node
                cur = head
                continue
            cur.next = node
            cur = node

        self.headNode = head

    def printList(self):
        self.headNode.printAfter()

if __name__ == '__main__':
    ll = LL(vals = [1])
    ll.headNode.printAfter()

