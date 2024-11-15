#!/usr/bin/python3

"""
CSV格式列变换

参考附件：data.csv
附件是一个CSV文件，请将每行按照列逆序排列后输出，不改变各元素格式（如周围空格布局等）。
"""

for line in open("data.csv", "r"):
    print(",".join(line.strip("\n").split(",")[::-1]))
