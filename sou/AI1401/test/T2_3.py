#!/usr/bin/python3

"""
实验 2-3 数组

实现一个n阶对称矩阵A采用一维数组a压缩存储，
压缩方法为按行优先顺序存放A的下三角和主对角线的各元素。
"""

import math
def disp(A):                     #输出二维数组A
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(" "+str(A[i][j]),end=' ')
        print()

def compression(A,a):              #将A压缩存储到a中
    n=len(A)
    for i in range(n):
        for j in range(0,i+1):
            a[i*(i+1)//2+j]=A[i][j]

#主程序
print("\n *********测试1**********")
n=3
A=[[1,2,3],[2,4,5],[3,5,6]]
C=[[None]*n for i in range(n)]
a=[0]*(n*(n+1)//2)
print(" A:"); disp(A)
print(" A压缩得到a")
compression(A,a)
print(" a:")
for i in range(len(a)):
    print(" "+str(a[i]),end=' ')
