## 一个很巧的办法
除下快慢指针的方式，还有一个很巧的办法。

每次判断当前节点的next是否它自己。如果不是，就把它的next指向它自己。
1. 如果有循环，在第一次遍历时，换会被打断，但是环的入口节点之后还会遍历到，届时则会返回True
2. 如果没有循环，则不会遍历到旧的节点，因此不会出现节点的next就是自己的情况。
附上一段代码，**这个方法也可以用于寻找环的入口节点，但是会破坏链表的原结构。**
```python
def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    curr = head
    while curr is not None:
        nextnode = curr.next
        if nextnode is head:
            return True
        curr.next = head
        curr = nextnode
    return False
```