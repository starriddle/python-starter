#!/usr/bin/python3

"""
实验 3-2 生成树

实现给定一个连通图，采用邻接表G存储，输出根结点为0的一棵深度优先生成树和一棵广度优先生成树，用相关数据进行测试

图邻接表类文件：AdjGraph.py
"""

from AdjGraph import AdjGraph, MAXV, INF  # 引用邻接表存储结构
from collections import deque  # 引用双端队列deque


def DFSTree(G, v):  # 邻接表G中从顶点v出发的深度优先遍历
    global visited
    global T1
    visited[v] = 1  # 置已访问标记
    for p in G.adjlist[v]:
        w = p.adjvex
        if visited[w] == 0:
            T1.append([v, w])  # 产生深度优先生成树的一条边
            DFSTree(G, w)  # 若w顶点未访问,递归访问它


def BFSTree(G, v):  # 邻接表G中从顶点v出发的广度优先遍历
    global T2
    global visited
    qu = deque()  # 创建空队列qu
    visited[v] = 1  # 置已访问标记
    qu.append(v)  # v进队
    while len(qu) > 0:
        v = qu.popleft()  # 队首元素出队并赋值给v
        for p in G.adjlist[v]:  # 依次检查v的所有邻接顶点w
            w = p.adjvex
            if visited[w] == 0:  # 若w未访问
                T2.append([v, w])  # 产生广度优先生成树的一条边
                visited[w] = 1  # 置已访问标记
                qu.append(w)  # w进队


if __name__ == '__main__':
    G = AdjGraph()
    n, e = 10, 12
    a = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 1, 1, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
         [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]
    print()
    print(" (1)由a创建邻接表G")
    G.CreateAdjGraph(a, n, e)
    print("  G:")
    G.DispAdjGraph()
    print(" (2)DFSTree构造深度优先生成树T1")
    T1 = []
    visited = [0] * MAXV
    DFSTree(G, 0)
    print("  T1:", T1)
    print(" (3)BFSTree构造广度优先生成树T2")
    T2 = []
    visited = [0] * MAXV
    BFSTree(G, 0)
    print("  T2:", T2)
