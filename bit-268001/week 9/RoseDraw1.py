#!/usr/bin/python3

"""
实例16: 玫瑰花绘制

用Python绘制一朵玫瑰花

turtle基本图形绘制

问题：因不同硬件 turtle 绘图实现方式不一致，部分硬件在绘制花朵时中心部位无法填充
处理：先绘制一遍花朵，将整个花朵轮廓填充颜色，然后在其上重新再绘制一遍花朵线条
"""

import turtle as t

# 初始设定
size = 0.2
t.setup(450 * 5 * size, 600 * 5 * size)
t.pencolor("black")
t.speed(100)


def degree_curve(n, radius, degree=1):
    """
    曲线绘制函数
    :param n: 曲线段数
    :param radius: 曲线半径
    :param degree: 曲线角度
    :return:
    """
    for i in range(n):
        t.left(degree)
        t.circle(radius, abs(degree))


def draw_flower(fill=False):
    """
    绘制花朵形状
    :param fill: True-仅填充，False-仅画线条
    :return:
    """
    t.penup()
    t.goto(-50 * 5 * size, 250 * 5 * size)  # 坐标 花朵起始位置
    t.setheading(0)
    if not fill:
        t.pendown()
    t.circle(200 * size, 30)
    degree_curve(60, 50 * size)
    t.circle(200 * size, 30)
    degree_curve(4, 100 * size)
    t.circle(200 * size, 50)
    degree_curve(50, 50 * size)
    t.circle(350 * size, 65)
    if fill:
        t.fillcolor("red")
        t.begin_fill()
    degree_curve(40, 70 * size)
    t.circle(150 * size, 50)
    degree_curve(20, 50 * size, -1)
    t.circle(400 * size, 60)
    degree_curve(18, 50 * size)
    t.forward(250 * size)
    t.right(150)
    t.circle(-500 * size, 12)
    t.left(140)
    t.circle(550 * size, 110)
    t.left(27)
    t.circle(650 * size, 100)
    t.left(130)
    t.circle(-300 * size, 20)
    t.right(123)
    t.circle(220 * size, 57)
    if fill:
        t.end_fill()


def draw_branch():
    """
    绘制枝条形状
    :return:
    """
    t.left(120)
    t.forward(280 * size)
    t.left(115)
    t.circle(300 * size, 33)
    t.left(180)
    t.circle(-300 * size, 33)
    degree_curve(70, 225 * size, -1)
    t.circle(350 * size, 104)
    t.left(90)
    t.circle(200 * size, 105)
    t.circle(-500 * size, 63)
    t.penup()
    t.goto(-16 * 5 * size, 64 * 5 * size)  # 坐标 花底位置
    t.pendown()
    t.left(160)
    degree_curve(20, 2500 * size)
    degree_curve(220, 250 * size, -1)


def draw_leaf1():
    """
    绘制第 1 片绿色叶子
    :return:
    """
    t.penup()
    t.goto(84 * 5 * size, 34 * 5 * size)  # 坐标 绿叶起始位置
    t.right(140)
    t.pendown()
    t.fillcolor('green')
    t.begin_fill()
    t.circle(300 * size, 120)
    t.left(60)
    t.circle(300 * size, 120)
    t.end_fill()
    t.penup()
    t.goto(-14 * 5 * size, -40 * 5 * size)  # 坐标 绿叶树枝起始位置
    t.pendown()
    t.right(85)
    t.circle(600 * size, 40)


def draw_leaf2():
    """
    绘制第 2 片绿色叶子
    :return:
    """
    t.penup()
    t.goto(-80 * 5 * size, -130 * 5 * size)  # 坐标 绿叶起始位置
    t.right(120)
    t.pendown()
    t.fillcolor('green')
    t.begin_fill()
    t.circle(300 * size, 110)
    t.left(70)
    t.circle(300 * size, 110)
    t.end_fill()
    t.penup()
    t.goto(36 * 5 * size, -144 * 5 * size)  # 坐标 绿叶树枝起始位置
    t.pendown()
    t.right(30)
    t.circle(-600 * size, 35)


draw_flower(True)
draw_flower(False)
draw_branch()
draw_leaf1()
draw_leaf2()
t.hideturtle()
t.done()
