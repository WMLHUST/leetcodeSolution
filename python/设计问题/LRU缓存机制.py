# 双向链表，配合hashtable
# hashtable负责根据key，在O(1)时间找到节点
# 双向链表用于记录访问顺序，并在O(1)时间内实现删除和插入
class LRUCache:
    class valNode:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.pre = None
            self.next = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.cur_capacity = 0
        self.head = self.valNode(0, 0)
        self.end = self.valNode(-1, -1)
        self.head.next = self.end
        self.end.pre = self.head

    def moveFirst(self, key):
        node = self.cache[key]
        if node.pre == self.head:
            return node.val

        if node.pre is not None:
            node.pre.next = node.next
        if node.next is not None:
            node.next.pre = node.pre

        self.head.next.pre = node
        node.next = self.head.next
        node.pre = self.head
        self.head.next = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        else:
            self.moveFirst(key)
            return self.head.next.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.cache:
            if self.cur_capacity>=self.capacity:
                node = self.end.pre
                # 前后连起来
                node.pre.next = self.end
                self.end.pre = node.pre
                del self.cache[node.key]
            else:
                self.cur_capacity += 1

            node = self.valNode(key, value)
            self.cache[key] = node
            # 新插入的放到第一个
            node.next = self.head.next
            node.pre = self.head

            self.head.next.pre = node
            self.head.next = node

        else:
            # 重复插入的也要放第一个
            self.moveFirst(key)
            self.head.next.val = value

        # self.printNext()
        # self.printPre()

    def printNext(self):
        cur = self.head
        while cur!=None:
            print(str(cur.key), end='->')
            cur = cur.next
        print('\n')

    def printPre(self):
        cur = self.head.next
        while cur!=None:
            print(str(cur.pre.key), end='<-')
            cur = cur.next
        print('\n')

cache = LRUCache( 2);
print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))
print(cache.put(3, 3))
print(cache.get(2))
print(cache.put(4, 4))
print(cache.get(1)) #这俩
print(cache.get(3))
print(cache.get(4))