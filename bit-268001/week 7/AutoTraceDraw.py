#!/usr/bin/python3

"""
实例11: 自动轨迹绘制

参考附件：latex.log
编写程序，根据文件接口解析参数绘制图形

数据文件格式（接口）：
- distance,turn,angle,R,G,B
  - 行进距离,转向(0-左转，1-右转),转向角度,RGB三通道颜色(0-1之间浮点数)
- 一行数据表示一条轨迹
  - 先以指定画笔颜色行进指定距离，再以指定转向和指定角度进行方向调整

优化：
读取数据后，每行数据边解析边绘制，降低时间复杂度，只需要1次循环
如果将所有数据全部解析完整后再开始绘制，则需要2次循环，耗时翻倍
"""

import turtle as t

t.title("自动轨迹绘制")
t.setup(800, 600)
t.pensize(5)
# 数据读取
f = open("trace.txt", "r")
lines = f.readlines()
f.close()
# 解析并绘制
for line in lines:
    data = list(map(eval, line.strip("\n").split(",")))  # 解析一行数据
    t.pencolor(data[3], data[4], data[5])  # 设置画笔颜色
    t.forward(data[0])  # 绘制线条
    t.right(data[2] * (1 if data[1] else -1))  # 转向
t.done()
