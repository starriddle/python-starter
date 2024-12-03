#!/usr/bin/python3

"""
实验 4-2 排序

实现随机产生20000个0~10000的整数序列a，
对于序列a分别采用直接插入排序、折半插入排序和希尔排序算法实现递增排序，
给出各个排序算法的执行时间（以秒为单位）
"""

import time
import random
import copy


def InsertSort(R):  # 对R[0..n-1]按递增有序进行直接插入排序
    for i in range(1, len(R)):
        if R[i] < R[i - 1]:  # 反序时
            tmp = R[i]  # 将R[i]保存到tmp中
            j = i - 1
            while j >= 0 and R[j] > tmp:  # 找到 R[j]<=tmp 或 j<0 为止
                R[j + 1] = R[j]  # 将大于 tmp 的元素后移
                j = j - 1  # j 向左移，继续比较
            R[j + 1] = tmp  # 将 tmp 插入到正确的位置


def BinInsertSort(R):  # 对R[0..n-1]按递增有序进行折半插入排序
    for i in range(1, len(R)):
        if R[i] < R[i - 1]:  # 反序时
            tmp = R[i]  # 将R[i]保存到tmp中
            low, high = 0, i - 1
            while low <= high:  # 在R[low..high]中折半查找插入位置high+1
                mid = (low + high) // 2  # 取中间位置
                if tmp < R[mid]:
                    high = mid - 1  # 插入点在左区间
                else:
                    low = mid + 1  # 插入点在右区间
            for j in range(i - 1, high, -1):  # 元素集中后移
                R[j + 1] = R[j]
            R[high + 1] = tmp  # 插入原来的R[i]


def ShellSort(R):  # 对R[0..n-1]按递增有序进行希尔排序
    d = len(R) // 2  # 增量置初值
    while d > 0:
        for i in range(d, len(R)):  # 对所有相隔d位置的元素组采用直接插入排序
            tmp = R[i]
            j = i - d
            while j >= 0 and R[j] > tmp:  # 找到R[j]<=tmp为止
                R[j + d] = R[j]  # 对相隔d位置的元素组排序
                j = j - d
            R[j + d] = tmp
        d = d // 2  # 递减增量


# 主程序
a = []
for i in range(20000):
    a.append(random.random() * 10000)
b = copy.deepcopy(a)
t1 = time.time()  # 获取开始时间
InsertSort(b)
t2 = time.time()  # 获取结束时间
print()
print("  直接插入排序的时间: %ds" % (t2 - t1))
b = copy.deepcopy(a)
t1 = time.time()  # 获取开始时间
BinInsertSort(b)
t2 = time.time()  # 获取结束时间
print("  折半插入排序的时间: %ds" % (t2 - t1))
b = copy.deepcopy(a)
t1 = time.time()  # 获取开始时间
ShellSort(b)
t2 = time.time()  # 获取结束时间
print("  希尔排序的时间:     %ds" % (t2 - t1))
