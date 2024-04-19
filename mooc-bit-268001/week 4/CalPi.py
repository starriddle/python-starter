#!/usr/bin/python3

"""
实例6：圆周率的计算

求解圆周率可以采用蒙特卡罗方法，
在一个正方形中撒点，根据在1/4圆内点的数量占总撒点数的比例计算圆周率值。

请以123作为随机数种子，获得用户输入的撒点数量，编写程序输出圆周率的值，保留小数点后6位。
"""

import random

dart = eval(input())
random.seed(123)
hits = 0
for i in range(dart):
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1:
        hits += 1
pi = 4 * hits / dart
print("{:.6f}".format(pi))
