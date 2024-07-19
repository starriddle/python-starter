#!/usr/bin/python3

"""
英文字符的鲁棒输入

获得用户的任何可能输入，将其中的英文字符进行打印输出，程序不出现错误。
"""

for c in input():
    if 'A' <= c <= 'Z' or 'a' <= c <= 'z':
        print(c, end="")
