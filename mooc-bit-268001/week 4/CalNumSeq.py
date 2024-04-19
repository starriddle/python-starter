#!/usr/bin/python3

"""
整数的加减和

编写程序计算如下数列的值：
1-2+3-4...966
其中，所有数字为整数，从1开始递增，奇数为正，偶数为负
"""

ret = 0
flag = 1
for i in range(1, 967):
    ret += i * flag
    flag = -flag
print(ret)
