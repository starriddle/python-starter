#!/usr/bin/python3

"""
斐波那契数列计算

计算斐波那契数列的值，具体功能如下：
1. 获取用户输入整数N，其中，N为正整数；
2. 计算斐波那契数列的值

如果将斐波那契数列表示为fbi(N)，对于整数N，值如下：
fbi(1)和fbi(2)的值是1，当N>2时，fbi(N) = fbi(N-1) + fbi(N-2)

请采用递归方式编写。
"""


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(eval(input())))
