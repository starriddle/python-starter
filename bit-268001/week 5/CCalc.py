#!/usr/bin/python3

"""
任意累积

计算任意个输入数字（中间以,分隔）的乘积

扩展

计算任意个输入数字（中间以,分隔）的连续 加减乘除
"""


def cadd(a, *b):
    for i in b:
        a += i
    return a


def csub(a, *b):
    for i in b:
        a -= i
    return a


def cmul(a, *b):
    for i in b:
        a *= i
    return a


def cdiv(a, *b):
    for i in b:
        a /= i
    return a


def ccalc():
    calc = input()
    print(eval("{}({})".format(calc, input())))


def main():
    print(eval("cmul({})".format(input())))


main()
ccalc()
