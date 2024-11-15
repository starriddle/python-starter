#!/usr/bin/python3

"""
实例16: 玫瑰花绘制

用Python绘制一朵玫瑰花

turtle基本图形绘制
"""

import turtle as t


# 定义一个曲线绘制函数
def degree_curve(n, radius, degree=1):
    for i in range(n):
        t.left(degree)
        t.circle(radius, abs(degree))


# 初始位置设定
size = 0.2
t.setup(450*5*size, 600*5*size)
t.pencolor("black")
t.fillcolor("red")
t.speed(100)
t.penup()
t.goto(-50*5*size, 250*5*size)  # 坐标 花朵起始位置
t.pendown()

# 绘制花朵形状
t.begin_fill()
t.circle(200*size,30)
degree_curve(60, 50*size)
t.circle(200*size,30)
degree_curve(4, 100*size)
t.circle(200*size,50)
degree_curve(50, 50*size)
t.circle(350*size,65)
degree_curve(40, 70*size)
t.circle(150*size,50)
degree_curve(20, 50*size, -1)
t.circle(400*size,60)
degree_curve(18, 50*size)
t.forward(250*size)
t.right(150)
t.circle(-500*size,12)
t.left(140)
t.circle(550*size,110)
t.left(27)
t.circle(650*size,100)
t.left(130)
t.circle(-300*size,20)
t.right(123)
t.circle(220*size,57)
t.end_fill()

# 绘制花枝形状
t.left(120)
t.forward(280*size)
t.left(115)
t.circle(300*size,33)
t.left(180)
t.circle(-300*size,33)
degree_curve(70, 225*size, -1)
t.circle(350*size,104)
t.left(90)
t.circle(200*size,105)
t.circle(-500*size,63)
t.penup()
t.goto(-16*5*size,64*5*size)  ## 坐标 花底位置
t.pendown()
t.left(160)
degree_curve(20, 2500*size)
degree_curve(220, 250*size, -1)

# 绘制一个绿色叶子
t.fillcolor('green')
t.penup()
t.goto(84*5*size,34*5*size)  # 坐标 绿叶起始位置
t.pendown()
t.right(140)
t.begin_fill()
t.circle(300*size,120)
t.left(60)
t.circle(300*size,120)
t.end_fill()
t.penup()
t.goto(-14*5*size,-40*5*size)  # 坐标 绿叶树枝起始位置
t.pendown()
t.right(85)
t.circle(600*size,40)

# 绘制另一个绿色叶子
t.penup()
t.goto(-80*5*size,-130*5*size)  # 坐标 绿叶起始位置
t.pendown()
t.begin_fill()
t.rt(120)
t.circle(300*size,115)
t.left(75)
t.circle(300*size,100)
t.end_fill()
t.penup()
t.goto(36*5*size,-144*5*size)  # 坐标 绿叶树枝起始位置
t.pendown()
t.right(30)
t.circle(-600*size,35)

# 绘制结束
t.done()
