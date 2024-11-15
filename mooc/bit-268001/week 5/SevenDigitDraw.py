#!/usr/bin/python3

"""
实例7：七段数码管绘制

七段数码管是一种展示数字的有效方式。
请用程序绘制当前系统时间对应的七段数码管，要求如下：

(1) 使用 time 库获得系统当前时间，格式如下：20190411
(2) 绘制对应的七段数码管
(3) 数码管风格不限

基本思路：
步骤 1：绘制单个数字对应的码管
步骤 2：获得当前系统时间，变成字符串，绘制对应的码管

思维方法：
- 模块化思维：确定接口，封装功能
- 规则化思维：抽象过程为规则，计算机自动执行
- 化繁为简：将大功能变小组合，分而治之
"""

import time
import turtle


def draw_gap(distance):
    turtle.penup()
    turtle.forward(distance)


def draw_line(distance, draw):
    draw_gap(distance / 10)
    turtle.pendown() if draw else turtle.penup()
    turtle.forward(distance*8/10)
    draw_gap(distance / 10)
    turtle.right(90)


def draw_digit(digit, distance):
    draw_line(distance, True) if digit in [2, 3, 4, 5, 6, 8, 9] else draw_line(distance, False)
    draw_line(distance, True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else draw_line(distance, False)
    draw_line(distance, True) if digit in [0, 2, 3, 5, 6, 8, 9] else draw_line(distance, False)
    draw_line(distance, True) if digit in [0, 2, 6, 8, 0] else draw_line(distance, False)
    turtle.left(90)
    draw_line(distance, True) if digit in [0, 4, 5, 6, 8, 9] else draw_line(distance, False)
    draw_line(distance, True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else draw_line(distance, False)
    draw_line(distance, True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else draw_line(distance, False)
    turtle.left(180)
    turtle.penup()
    turtle.forward(distance/2)


def draw_date(date, distance):
    turtle.pencolor("red")
    for i in date:
        if i == "-":
            turtle.write("年", align="left", font=("Noto Sans CJK SC", 20, "bold"))
            turtle.pencolor("green")
            turtle.forward(distance)
        elif i == "=":
            turtle.write("月", align="left", font=("Noto Sans CJK SC", 20, "bold"))
            turtle.pencolor("blue")
            turtle.forward(distance)
        elif i == "+":
            turtle.write("日", align="left", font=("Noto Sans CJK SC", 20, "bold"))
        else:
            draw_digit(eval(i), distance)


def main():
    turtle.setup(850, 300)
    turtle.penup()
    turtle.back(400)
    turtle.pensize(5)
    draw_date(time.strftime("%Y-%m=%d+", time.localtime()), 50)
    turtle.hideturtle()
    turtle.done()


main()
