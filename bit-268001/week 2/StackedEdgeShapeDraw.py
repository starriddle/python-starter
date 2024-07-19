#!/usr/bin/python3

"""
turtle叠边形绘制

使用turtle库，绘制一个叠边形，其中，叠边形内角为100度。

分析：
内角100度，外角80度，720 / 80 = 9，9条边绕2圈回到起点
9个顶点处于同一个圆且分布均匀，与圆心（中心点）连线后每个角为40度
每条边对应圆心角为80度，形成底边为叠边形 边长为a 顶角为80度的等腰三角形
"""

import turtle as t

t.setup(450, 350)

# 图形居中
t.penup()
t.goto(-100, -119.18)  # x=-(a/2) y=-(a/2*tan50)
t.pendown()

t.pensize(5)

# 开始绘制
for i in range(9):
    t.forward(200)  # a=200
    t.left(80)
t.done()
