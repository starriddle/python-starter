#!/usr/bin/python3

"""
文件行数

参考附件：latex.log
打印输出附件文件的有效行数，注意：空行不计算为有效行数。
"""

f = open("latex.log", "r")
lines = f.readlines()
f.close()
count = 0
for line in lines:
    if len(line.strip("\n")) > 0:
        count += 1
print("共{}行".format(count))
