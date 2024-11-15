#!/usr/bin/python3

"""
数字形式转换

获得用户输入的一个正整数输入，输出该数字对应的中文字符表示。
0到9对应的中文字符分别是：零一二三四五六七八九
"""

number = '零一二三四五六七八九'
s = input("请输入一个正整数：")
for c in s:
    print(number[eval(c)], end="")
print()
