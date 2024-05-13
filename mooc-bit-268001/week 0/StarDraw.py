#!/usr/bin/python3

# Python Demo 五角星

from turtle import *

pu()
goto(-100, 0)
pd()
color("blue", "red")

begin_fill()
for i in range(5):
    fd(200)
    rt(144)
end_fill()
done()
