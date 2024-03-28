#!/usr/bin/python3

"""
turtle风轮绘制

使用turtle库，绘制一个风轮效果，其中，每个风轮内角为45度，风轮边长150像素。
"""

import turtle as t

t.setup(450, 350)

t.pensize(5)

# 开始绘制
for i in range(4):
    t.left(45)
    t.forward(150)
    t.left(90)
    t.circle(150, 45)
    t.right(90)
    t.backward(150)
t.done()
