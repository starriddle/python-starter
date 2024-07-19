#!/usr/bin/python3

"""
字符串分段组合

获得输入的一个字符串s，以字符减号(-)分割s，将其中首尾两段用加号(+)组合后输出。
"""

strs = input().split("-")
print(strs[0] + "+" + strs[-1])
