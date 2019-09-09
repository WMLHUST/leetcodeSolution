# coding: utf-8

def min_heapify(a, size, root):
    left = 2*root + 1
    right = 2*root + 2

    # 选取root, left, right中三者较小的，作为该子堆的根节点
    min_node = root
    # 子节点有可能不存在，因此要判断一下<size
    if left < size and a[left]<a[min_node]:
        min_node = left
    if right < size and a[right]<a[min_node]:
        min_node = right

    if min_node!=root:
        # 需要交换，然后调整对应的子树
        a[root], a[min_node] = a[min_node], a[root]
        min_heapify(a, size, min_node)

# 构建堆，构建堆也是从最后一个有子节点的节点开始adjust
def build_min_heap(a):
    size = len(a)
    for i in range((size-2)//2, -1, -1):
        min_heapify(a, size, i)

# 降序
def heap_sort(a):
    build_min_heap(a)
    print("min_heapify: ", a)
    for i in range(len(a)-1, -1, -1):
        a[0], a[i] = a[i], a[0]
        min_heapify(a, i, 0)

# 堆的插入，要调整相关的子堆节点，直到根节点
# 还是O(log(n))
def heap_insert(a, num):
    a.append(num)
    cur = len(a) - 1
    cur_parent = (cur-1) // 2
    while cur_parent>=0:
        # 如果当前的父节点，小于子节点，（满足小顶堆的条件）不用调整
        if a[cur_parent] <= num:
            break

        # 将父节点下移到子节点，然后继续调整父节点的父节点
        a[cur] = a[cur_parent]
        cur = cur_parent
        cur_parent = (cur_parent-1) // 2

    a[cur] = num

a = [16, 14, 10, 8, 7, 6, 7, 2, 4]
build_min_heap(a)
print(a)
heap_insert(a, 1)
print(a)


