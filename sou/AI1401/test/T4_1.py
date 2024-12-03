#!/usr/bin/python3

"""
实验 4-1 查找

实现对一个递增有序表进行折半查找，输出成功找到其中每个元素的查找序列，用相关数据进行测试
"""


def BinSearch(R, k):  # 拆半查找非递归算法
    L = []  # 查找序列
    low, high = 0, len(R) - 1
    while low <= high:  # 当low<=high时，继续查找
        mid = (low + high) // 2  # 取中间位置
        L.append((mid, R[mid]))  # 将下标和元素二元组添加到查找序列中
        if R[mid] == k:  # 找到元素
            return L  # 返回查找序列
        elif R[mid] > k:  # 中间元素大于查找元素
            high = mid - 1  # 在左半部分继续查找
        else:  # 中间元素小于查找元素
            low = mid + 1  # 在右半部分继续查找
    L.append((-1, None))  # 没有找到元素
    return L  # 返回查找序列


# 主程序
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print()
print("  整数序列:", a)
for i in range(len(a)):
    L = BinSearch(a, a[i])
    print("  查找%d的查找序列:" % (a[i]), end='')
    print(L)
