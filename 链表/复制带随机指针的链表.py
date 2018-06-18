# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):

    def prettyPrintLinkedList(self, node):
        label_str = ""
        id_str = ""
        random_str = ""
        while node:
            label_str += str(node.label) + "->"
            id_str += str(id(node)) + "->"
            if node.random == None:
                random_str += "0" + "->"
            else:
                random_str += str(id(node.random)) + "->"
            # print(str(node.label) + "->", end='')
            # print(str(id(node)) + ">", end="")
            # print(str(id(node.random)) + ">", end="")
            node = node.next
        print("label: ", label_str)
        print("id: ", id_str)
        print("random: ", random_str)

        # if node:
        #     print(node.label)
        # else:
        #     print("Empty LinkedList")

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head==None:
            return head

        # 复制节点
        cur = head
        while cur!=None:
            dup_cur = RandomListNode(cur.label)
            dup_cur.next = cur.next
            cur.next = dup_cur

            cur = dup_cur.next

        # 复制random指针
        # 这一步和恢复链表原状不能同时做，因为后面的节点随机指针可能指向前面。。坑啊，调了好久。。
        cur = head
        while cur!=None:
            cur.next.random = cur.random.next if cur.random!=None else None
            cur = cur.next.next

        # 恢复链表原状
        res = head.next
        cur = head
        while cur!=None:
            tmp = cur.next
            cur.next = cur.next.next
            tmp.next = tmp.next.next if tmp.next!=None else None
            cur = cur.next

        self.prettyPrintLinkedList(head)
        self.prettyPrintLinkedList(res)
        return res

def hasNode(head, node):
    while head!=None:
        if node == head:
            return True
        head = head.next
    return False

def compare(head1, head2):
    ori_head1 = head1
    while head1!=None and head2!=None:
        if head1.label!=head2.label or hasNode(ori_head1, head2):
            return False
        if head1.random!=None and (head1.random.label!=head2.random.label or hasNode(ori_head1, head2.random)):
            return False
        if head1.random==None and head2.random!=None:
            return False

        head1 = head1.next
        head2 = head2.next
    return True


head = RandomListNode(-1)
node1 = RandomListNode(0)
head.next = node1
node2 = RandomListNode(1)
node1.next = node2
node3 = RandomListNode(2)
node2.next = node3

# head.random = node3
# node1.random = node3
# node2.random = node3
node3.random = node2

copy_head = Solution().copyRandomList(head)



