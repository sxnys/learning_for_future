'''
快速排序
最坏情况：O(n^2)
平均情况：O(nlogn)
优化：
1、首末中位置处三数，取中值
2、随机选取基准数
'''

import random

# 基数每次选第一个数
def quicksort(lst, left, right):
    if left > right:
        return
    i, j = left, right
    base = lst[left]
    while i != j:
        # 以最左边为基准数，必须先从右边移动，因为涉及到 i 和 j 谁主动去遇到对方
        # j 先动，就确保 j 先遇到 i，此时 i 处的值一定是比基准数小的（上轮移动i，j交换过），
        # 最后才能交换i处值和基准数
        while i < j and lst[j] >= base:
            j -= 1
        while i < j and lst[i] <= base:
            i += 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[left], lst[i] = lst[i], lst[left]
    quicksort(lst, left, i - 1)
    quicksort(lst, i + 1, right)


if __name__ == '__main__':
    lst = [random.randint(1, 100) for _ in range(50)]
    quicksort(lst, 0, len(lst) - 1)
    print(lst)