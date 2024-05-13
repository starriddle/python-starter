#!/usr/bin/python3

"""
文件关键行数

参考附件：latex.log
统计附件文件中关键行的数量。
关键行指一个文件中包含的不重复行。
关键行数指一个文件中包含的不重复行的数量。
"""

f = open("latex.log", "r")
lines = f.readlines()
f.close()
count = len(set(lines))
print("共{}关键行".format(count))
