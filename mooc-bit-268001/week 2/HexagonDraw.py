#!/usr/bin/python3

"""
turtle六边形绘制

使用turtle库，绘制一个六边形。
"""


import turtle as t

t.setup(450, 350)

# 图形居中
t.penup()
t.right(120)
t.forward(100)
t.left(120)
t.pendown()

t.pensize(5)

# 开始绘制
for i in range(6):
    t.forward(100)
    t.left(60)
t.done()
