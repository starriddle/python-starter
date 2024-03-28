#!/usr/bin/python3

"""
turtle正方形绘制

使用turtle库，绘制一个正方形。
"""

import turtle as t

t.setup(450, 350)

# 图形居中
t.penup()
t.goto(-50, -50)
t.pendown()

t.pensize(5)

# 开始绘制
for i in range(4):
    t.forward(100)
    t.left(90)
t.done()
