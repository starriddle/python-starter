#!/usr/bin/python3

"""
Python蟒蛇绘制

使用turtle库，绘制一个蟒蛇形状的图形。
"""

import turtle as t

t.setup(800, 350)

# 图形居中
t.penup()
t.forward(-300)
t.pendown()

t.pensize(20)
t.pencolor("purple")

# 开始绘制
t.setheading(-40)
for i in range(4):
    t.circle(50, 80)
    t.circle(-50, 80)
t.circle(50, 80/2)
t.forward(50)
t.circle(50 * 2/3)
t.done()
