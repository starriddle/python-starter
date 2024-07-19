#!/usr/bin/python3

"""
CSV格式清洗与转换

参考附件：data.csv
附件是一个CSV格式文件，提取数据进行如下格式转换：
（1）按行进行倒序排列；
（2）每行数据倒序排列；
（3）使用分号（;）代替逗号（,）分割数据，无空格；
按照上述要求转换后将数据输出。

示例：
输入(以下内容在文件中)
1,2,3
4,5,6
7,8,9

输出
9;8;7
6;5;4
3;2;1
"""

f = open("data.csv", "r")
lines = f.readlines()
f.close()
for line in lines[::-1]:
    ls = []
    for item in line.strip("\n").split(",")[::-1]:
        ls.append(item.strip(" "))
    print(";".join(ls))
