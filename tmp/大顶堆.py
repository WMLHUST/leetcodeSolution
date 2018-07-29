# coding: utf-8

# 关键：数组索引为n的节点的父节点：(n-1)/2，子节点：左: 2n+1，右: 2n+2
# 调整root索引为根节点的堆。
# 递归调整，还是比较简单的
def max_heapify(heap, size, root):
    left = 2*root + 1
    right = 2*root + 2
    larger = root
    if left < size and heap[larger] < heap[left]:
        larger = left
    if right < size and heap[larger] < heap[right]:
        larger = right

    if larger != root:
        heap[larger], heap[root] = heap[root], heap[larger]
        max_heapify(heap, size, larger)

# 构建堆，构建堆也是从最后一个有子节点的节点开始adjust
def build_max_heap(heap):
    size = len(heap)
    # 从(size-2)//2这里开始调整，为啥从下往上调整。。
    # 必须得从下往上，顺着来，比如root跟right交换了，等遍历到left时，由于left为根节点的堆还未调整，调整后可能会影响之前的root，间接也可能影响到right
    # 而从下往上，由于左右节点对应的子堆已经调整好了，所以root跟left交换，只会影响到left分支，不会影响到right
    for i in range((size-2)//2, -1, -1):
        max_heapify(heap, size, i)

# 堆排序，就是先构建好堆，然后每次出堆一个，由于是大顶堆，所以每次出的都是最大值
# 大顶堆，用于升序排序
def heap_sort(a):
    build_max_heap(a)
    print("heapify: ", a)
    for i in range(len(a)-1, -1, -1):
        a[0], a[i] = a[i], a[0]
        max_heapify(a, i, 0)

# 堆的插入，每次放到最后，然后调整对应的父节点，直到根结点
# 前提，a已经是个堆，否则是无意义的
def heap_insert(a, num):
    # 现在num只是占个位
    a.append(num)
    cur = len(a) - 1
    cur_parent = (cur-1)//2
    while cur_parent>=0:
        # 不影响父节点，不用调整
        if a[cur_parent] > num:
            break

        # cur_parent下移到子节点，把位置让出来
        a[cur] = a[cur_parent]

        # 递归下一个parent
        cur = cur_parent
        cur_parent = (cur_parent-1) // 2

    a[cur] = num



a = [30, 50, 57, 77, 62, 78, 94, 80, 84]
build_max_heap(a)
print(a)
heap_insert(a, 99)
print(a)