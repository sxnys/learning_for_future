'''
堆排序（以最小堆为例）
heap[int] 为维护的堆，堆编号从1开始
lst[] 为需要排序的数组
'''

import random

heap = [None]
n = 0    # 堆需要维护的最大长度

## shiftup 和 shiftdown 是建堆和维护堆的基本操作
# 向上调整，维护堆结构
def shiftup(i):
    while i > 1:
        father_i = i // 2
        if heap[i] < heap[father_i]:
            heap[i], heap[father_i] = heap[father_i], heap[i]
        else:
            break
        i = father_i

# 向下调整，维护堆结构
def shiftdown(i):
    global n
    t = 0
    # 保证有子节点（至少要有左子节点）
    while i * 2 <= n:
        t = i * 2 if heap[i] > heap[i*2] else i
        
        # 如果有右子节点
        if i * 2 + 1 <= n:
            t = i * 2 + 1 if heap[i*2+1] < heap[t] else t

        if t != i:
            heap[i], heap[t] = heap[t], heap[i]
            i = t
        else:
            break


## 建堆
# 1、边加新元素边维护
def build1(lst):
    global n
    for v in lst:
        n += 1
        heap.append(v)
        shiftup(n)

# 2、先把所有数填进完全二叉树，再维护
def build2(lst):
    global n
    for v in lst:
        n += 1
        heap.append(v)

    for i in range(n//2, 0, -1):
        shiftdown(i)


# 删除堆顶元素
def deleteTop():
    global n
    top = heap[1]
    heap[1] = heap[n]
    n -= 1
    shiftdown(1)
    return top


## 堆排序
# 1、每次弹堆顶
def heapsort1(lst):
    global n
    build1(lst)
    res = []
    while n > 0:
        res.append(deleteTop())
    return res

# 2、从小到大排建最大堆，反之建最小堆；交换堆顶和堆尾的两数即可
def heapsort2(lst):
    global n
    build1(lst)
    while n > 1:
        heap[1], heap[n] = heap[n], heap[1]
        n -= 1
        shiftdown(1)
    return heap[1:]

if __name__ == '__main__':
    lst = [random.randint(1, 100) for _ in range(10)]
    print(lst)
    # build1(lst)
    # print(heap)
    print(heapsort2(lst))