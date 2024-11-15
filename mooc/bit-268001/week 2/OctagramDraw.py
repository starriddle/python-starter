#!/usr/bin/python3

"""
turtle八角图形绘制

使用turtle库，绘制一个八角图形。

分析：
八角星形内角 360 / 8 = 45 度，外角 135 度
8个顶点位于同一个圆上，8条边对应的圆心角为 135度
"""

import turtle as t

t.setup(450, 350)

# 图形居中
t.penup()
t.goto(-100, -41.42)  # x=-(a/2) y=-(a/2*tan22.5)
t.pendown()

t.pensize(5)

# 开始绘制
for i in range(8):
    t.forward(200)  # a = 200
    t.left(135)
t.done()
