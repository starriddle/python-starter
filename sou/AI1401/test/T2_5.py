#!/usr/bin/python3

"""
实验 2-4 递归

输入一个正整数 n (n>5)，随机产生 n 个 1~99 的整数，采用递归算法求其中的最大整数
"""

import random

def solve():
    print()
    n = int(input("  n: "))
    a = random.sample(range(0, 100), n)
    print("  整数序列:", a)
    res = Max(a, n - 1)
    print("  最大整数：%d" % (res))
    print()


def Max(a, i):
    return a[0] if i == 0 else max(a[i], Max(a, i - 1))

# 主程序
solve()
