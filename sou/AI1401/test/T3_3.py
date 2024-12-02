#!/usr/bin/python3

"""
实验 3-3 图

利用文件gin.txt中的图求出以顶点0为源点的所有单源最短路径及其长度。

图文件：gin.txt
图邻接矩阵类程序文件：ExpMatGraph.py
"""

from ExpMatGraph import MatGraph, INF, MAXV


def Dijkstra(g, v):  # 求从v到其他顶点的最短路径
    S = [0] * MAXV  # 初始化集合S
    dist = [INF] * MAXV  # 初始化最短路径长度数组，将v到所有顶点的距离设为 INF
    path = [-1] * MAXV  # 初始化最短路径数组，将所有顶点前驱都设为-1
    for i in range(g.n):  # 初始化dist和path
        if g.edges[v][i] < INF:  # 如果v到i有边
            dist[i] = g.edges[v][i]  # 将v到i的距离存入dist数组
            path[i] = v  # 将路径上顶点i的前驱置为v
    S[v] = 1  # 将源点v加入集合S
    for i in range(g.n - 1):  # 循环n-1次
        mindist = INF  # 初始化最小距离
        u = -1  # 初始化u
        for j in range(g.n):  # 寻找离v最近的顶点u
            if S[j] == 0 and dist[j] < mindist:  # 如果顶点j不在集合S中且v到j的距离小于mindist
                u = j  # 将顶点j赋值给u
                mindist = dist[j]  # 将v到j的距离赋值给mindist
        S[u] = 1  # 将顶点u加入集合S
        for j in range(g.n):  # 更新dist和path
            if S[j] == 0 and dist[u] + g.edges[u][j] < dist[j]:  # 如果顶点j不在集合S中且v到u再到j的距离小于v到j的距离
                dist[j] = dist[u] + g.edges[u][j]  # 更新v到j的距离
                path[j] = u  # 更新路径上顶点j的前驱为u
    DispAllPath(dist, path, S, v, g.n)  # 输出从顶点v出发的所有最短路径


def DispAllPath(dist, path, S, v, n):  # 输出从顶点v出发的所有最短路径
    for i in range(n):  # 循环输出从顶点v到i的路径
        if S[i] == 1 and i != v:
            apath = []
            print("    从%d到%d最短路径长度: %d \t路径:" % (v, i, dist[i]), end=' ')
            apath.append(i)  # 添加路径上的终点
            k = path[i];
            if k == -1:  # 没有路径的情况
                print("无路径")
            else:  # 存在路径时输出该路径
                while k != v:
                    apath.append(k)  # 顶点k加入到路径中
                    k = path[k]
                apath.append(v)  # 添加路径上的起点
                apath.reverse()  # 逆置apath
                print(apath)  # 输出最短路径


# 主程序
g = MatGraph()
g.CreateMatGraph()
print()
print("  图g:")
g.DispMatGraph()
v = 0
print("  求解结果")
Dijkstra(g, v)
