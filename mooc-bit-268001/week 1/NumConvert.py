#!/usr/bin/python3

number = '零一二三四五六七八九'
s = input("请输入一个正整数：")
for c in s :
    print(number[eval(c)], end="")
print()