#!/usr/bin/python3

"""
文件独特行数

参考附件：latex.log
统计附件文件中与其他任何其他行都不同的行的数量，即独特行的数量。
"""

f = open("latex.log", "r")
lines = f.readlines()
f.close()
s = set(lines)
for line in s:
    lines.remove(line)
s -= set(lines)
print("共{}独特行".format(len(s)))
