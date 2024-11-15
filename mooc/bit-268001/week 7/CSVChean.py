#!/usr/bin/python3

"""
CSV格式数据清洗

参考附件：data.csv
附件是一个CSV文件，其中每个数据前后存在空格，请对其进行清洗，要求如下：
（1）去掉每个数据前后空格，即数据之间仅用逗号(,)分割；
（2）清洗后打印输出。
"""

for line in open("data.csv", "r"):
    s = ""
    for item in line.strip("\n").split(","):
        s += item.strip(" ") + ","
    print(s[0:-1])
