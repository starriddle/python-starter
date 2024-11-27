#!/usr/bin/python3

"""
实验 2-2 顺序串

实现给定两个字符串s和t，求串t在串s中不重叠出现的次数，如果不是子串则返回0。

例如，s="aaaab"，t="aa"，则t在s中出现2次。
"""

MaxSize = 100

# 基于BF算法
def StrCount1(s, t):  # BF算法求解
    i, cnt = 0, 0
    while i < len(s) - len(t) + 1:
        j, k = i, 0
        while j < len(s) and k < len(t) and s[j] == t[k]:
            j, k = j + 1, k + 1
        if k == len(t):  # 找到一个子串
            cnt += 1  # 累加出现的次数
            i = j  # i从j开始
        else:
            i += 1  # i增加1
    return cnt

# 基于KMP算法
def GetNext(t, next):  # 由模式串t求出next值
    j, k = 0, -1
    next[0] = -1
    while j < len(t) - 1:
        if k == -1 or t[j] == t[k]:
            j, k = j + 1, k + 1
            next[j] = k
        else:
            k = next[k]

def StrCount2(s, t):
    i, j = 0, 0
    cnt = 0
    next = [0] * MaxSize
    GetNext(t, next)  # 求next数组
    while i < len(s) and j < len(t):
        if j == -1 or s[i] == t[j]:
            i, j = i + 1, j + 1
        else:
            j = next[j]
        if j >= len(t):  # 找到一个子串
            cnt += 1  # 累加出现的次数
            j = 0
    return cnt

# 主程序
print()
print(" 测试1")
s = "aaaab"
t = "aa"
print("   s: " + s + " t:" + t)
print("    BF: t在s中出现次数=%d" % (StrCount1(s, t)))
print("   KMP: t在s中出现次数=%d" % (StrCount2(s, t)))
print(" 测试2")
s = "abcabcdabcdeabcde"
t = "abcd"
print("   s: " + s + " t:" + t)
print("    BF: t在s中出现次数=%d" % (StrCount1(s, t)))
print("   KMP: t在s中出现次数=%d" % (StrCount2(s, t)))
print(" 测试3")
s = "abcABCDabc"
t = "abcd"
print("   s: " + s + " t:" + t)
print("    BF: t在s中出现次数=%d" % (StrCount1(s, t)))
print("   KMP: t在s中出现次数=%d" % (StrCount2(s, t)))
