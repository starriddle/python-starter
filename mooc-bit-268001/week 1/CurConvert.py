#!/usr/bin/python3

CurStr = input("请输入带有符号的金额：")
if CurStr[0:3] == "RMB" :
    USD = eval(CurStr[3:]) / 6.78
    print("转换后的金额是：USD{:.2f}".format(USD))
elif CurStr[0:3] == "USD" :
    RMB = eval(CurStr[3:]) * 6.78
    print("转换后的金额是：RMB{:.2f}".format(RMB))
else :
    print("输入格式错误")