#!/usr/bin/python3

"""
Python Demo 五角星

不同硬件 turtle 绘图实现方式不一致，
有的硬件绘制时，内部正五边形可能无法填充
需要对其重新进行填充

方法一：
1. 正常绘制五角星
2. 再次绘制一个包含内部正五边形的等腰三角形
注意：隐藏内部正五边形的边，会有较好的显示效果
"""

from turtle import *

pu()
goto(-100, 0)
pd()
color("blue", "red")

# 绘制五角星，边长 200
begin_fill()
for i in range(5):
    pd()
    fd(76.9)
    pu()
    fd(46.2)  # 隐藏内部正五边形的边
    pd()
    fd(76.9)
    rt(144)
end_fill()

# 绘制包含内部正五边形的等腰三角形
pu()
fd(76.9)
begin_fill()
for i in range(2):
    pu()
    fd(46.2)  # 隐藏内部正五边形的边
    pd()
    fd(76.9)
    rt(144)
    fd(76.9)
pu()
fd(46.2)  # 隐藏内部正五边形的边
end_fill()

done()
