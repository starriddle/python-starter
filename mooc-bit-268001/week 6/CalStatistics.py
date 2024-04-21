#!/usr/bin/python3

"""
实例9：基本统计值计算

获取以逗号分隔的多个数据输入（输入为一行），计算基本统计值（计数、最值、和、平均值、标准差、中位数）
平均值、标准差保留小数点后两位。
"""


def get_numbers():  # 获取数值
    num_list = []
    num_str = input("请输入多个数值（以 , 分隔）：")
    for i in num_str.split(","):
        num_list.append(eval(i))
    return num_list


def mean(numbers):  # 计算算术平均值
    return sum(numbers) / len(numbers)


def sd(numbers, average):  # 计算样本标准差
    dev = 0
    for i in numbers:
        dev += (i - average) ** 2
    return (dev / (len(numbers) - 1)) ** 0.5


def median(numbers):  # 计算中位数
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        return (numbers[size // 2] + numbers[size // 2 - 1]) / 2
    else:
        return numbers[size // 2]


n = get_numbers()
m = mean(n)
print("个数:{}，总和:{}，最大值:{}，最小值:{}，平均值:{:.2f}，样品标准差:{:.2f}，中位数:{}"
      .format(len(n), sum(n), max(n), min(n), m, sd(n, m), median(n)))
