#!/usr/bin/python3

"""
实验 3-3 图

图邻接矩阵类
"""

MAXV = 100  # 表示最多顶点个数
INF = 0x3f3f3f3f  # 表示∞
visited = [0] * MAXV  # 全局访问标志数组


class MatGraph:  # 图邻接矩阵类
    def __init__(self, n=0, e=0):  # 构造方法
        self.n = n  # 顶点数
        self.e = e  # 边数
        self.edges = [[INF] * MAXV for i in range(MAXV)]  # 邻接矩阵数组
        for i in range(MAXV):  # 主对角线元素置为0
            self.edges[i][i] = 0

    def CreateMatGraph(self):  # 通过文件数据建立图的邻接矩阵
        f = open("gin.txt", "r")
        tmp = f.readline().split()  # 读取第1行
        self.n = int(tmp[0])
        self.e = int(tmp[1])
        while True:
            tmp = f.readline().split()
            if not tmp: break
            i, j, w = int(tmp[0]), int(tmp[1]), int(tmp[2])
            self.edges[i][j] = w
            self.edges[j][i] = w
        f.close()

    def DispMatGraph(self):  # 输出图
        for i in range(self.n):
            for j in range(self.n):
                if self.edges[i][j] == INF:
                    print("%4s" % ("∞"), end=' ')
                else:
                    print("%5d" % (self.edges[i][j]), end=' ')
            print()


if __name__ == '__main__':
    g = MatGraph()
    g.CreateMatGraph()
    g.DispMatGraph()
