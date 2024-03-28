#!/usr/bin/python3

"""
turtle八边形绘制

使用turtle库，绘制一个八边形。

分析：
八边形外角 360 / 8 = 45 度，内角 135 度
"""

import turtle as t

t.setup(450, 350)

# 图形居中
t.penup()
t.goto(-50, -120.71)  # x=-(a/2) y=-(a/2+a/sqrt(2))
t.pendown()

t.pensize(5)

# 开始绘制
for i in range(8):
    t.forward(100)  # a=100
    t.left(45)
t.done()
