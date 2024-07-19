#!/usr/bin/python3

"""
文本的平均列数

参考附件：latex.log
打印输出附件文件的平均列数，计算方法如下：
（1）有效行指包含至少一个字符的行，不计算空行；
（2）每行的列数为其有效字符数；
（3）平均列数为有效行的列数平均值，采用四舍五入方式取整数进位。
"""

f = open("latex.log", "r")
lines = f.readlines()
f.close()
total = 0
count = 0
for line in lines:
    n = len(line.strip("\n"))
    if n > 0:
        total += n
        count += 1
print("{:.0f}".format(total / count))
