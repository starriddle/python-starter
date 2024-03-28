#!/usr/bin/python3

"""
货币转换

人民币和美元是世界上通用的两种货币之一，写一个程序进行货币间币值转换，其中：
人民币和美元间汇率固定为：1美元 = 6.78人民币。
程序可以接受人民币或美元输入，转换为美元或人民币输出。人民币采用RMB表示，美元USD表示，符号和数值之间没有空格。

注意：
(1) 这是一个OJ题目，获得输入请使用input() ；
"""

CurStr = input("请输入带有符号的金额：")
if CurStr[0:3] == "RMB":
    USD = eval(CurStr[3:]) / 6.78
    print("转换后的金额是：USD{:.2f}".format(USD))
elif CurStr[0:3] == "USD":
    RMB = eval(CurStr[3:]) * 6.78
    print("转换后的金额是：RMB{:.2f}".format(RMB))
else:
    print("输入格式错误")
