#!/usr/bin/python3

"""
随机密码生成

完成如下功能：
以整数17为随机数种子，获取用户输入整数N为长度，产生3个长度为N位的密码，密码的每位是一个数字。
每个密码单独一行输出。

产生密码采用random.randint()函数
random.randint(a,b) 随机生成范围 [a,b] 内的整数
"""

import random


def genpwd(length):
    return random.randint(10**(length-1), 10**length-1)


n = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(n))
