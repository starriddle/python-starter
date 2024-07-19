#!/usr/bin/python3

"""
数字的鲁棒输入

获得用户输入的一个数字，可能是浮点数或复数，如果是整数仅接收十进制形式，且只能是数字。
对输入数字进行平方运算，输出结果。

要求：
（1）无论用户输入何种内容，程序无错误；
（2）如果输入有误，请输出"输入有误"。

注意：
complex()和complex(eval())之间的比较将能够排除非数字类型的输入。
不能直接使用eval()，否则，用户可以通过输入表达式（如100**2）输入数字，与要求不同（在实际应用中带来安全隐患）。
"""


def robust1():
    s = input()
    flag = True
    try:
        num = complex(s)
        if num.imag == 0:  # 不含虚部复数，即为实数
            for c in s:  # 仅限数字和小数点
                if '0' <= c <= '9' or c == '.':
                    continue
                else:
                    flag = False
            if flag and s.count(".") <= 1:  # 最多一个小数点
                print(eval(s) ** 2)
            else:
                flag = False
        else:  # 含虚部复数，直接计算
            print(num ** 2)
    except:
        flag = False
    if not flag:  # 校验不通过，非数字
        print("输入有误")


def robust2():
    s = input()
    try:
        if complex(s) == complex(eval(s)):
            print(eval(s) ** 2)
    except:
        print("输入有误")


robust1()
robust2()
