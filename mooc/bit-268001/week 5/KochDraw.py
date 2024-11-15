#!/usr/bin/python3

"""
实例8：科赫雪花小包裹

描述：
科赫曲线，也叫雪花曲线。绘制科赫曲线

获得用户输入的整数N，作为阶，绘制N阶科赫曲线
"""

import turtle


def koch(size, n):
    if n == 0:
        turtle.forward(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)


def snow(size, n):
    side = ((size * 2 / 3 ** 0.5 // 50) + 1) * 50
    print(side)
    turtle.setup(side, side)
    turtle.penup()
    turtle.goto(-size / 2, size / 2 / pow(3, 0.5))
    turtle.pendown()
    turtle.pensize(2)
    koch(size, n)
    turtle.right(120)
    koch(size, n)
    turtle.right(120)
    koch(size, n)
    turtle.hideturtle()
    turtle.done()


length = input("请输入科赫雪花曲线长度：")
fact = input("请输入科赫雪花曲线阶数：")
print("开始绘制科赫雪花……")
snow(eval(length), eval(fact))
