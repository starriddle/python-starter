#!/usr/bin/python3

"""
Hello World的条件输出

获得用户输入的一个整数，参考该整数值，打印输出"Hello World"，要求：

如果输入值是0，直接输出"Hello World"
如果输入值大于0，以两个字符一行方式输出"Hello World"（空格也是字符）
如果输入值小于0，以垂直方式输出"Hello World"
"""

s = "Hello World"
n = input()
if eval(n) == 0:
    print(s)
elif eval(n) > 0:
    for i in range(len(s) // 2 + len(s) % 2):  # 根据字符串长度按2个字符分组
        print(s[i * 2:(i + 1) * 2])
else:
    for c in s:
        print(c)
