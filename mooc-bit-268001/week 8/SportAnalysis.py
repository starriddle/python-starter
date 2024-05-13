#!/usr/bin/python3

"""
实例13: 体育竞技分析

比赛规则
- 双人击球比赛: A & B，回合制，5 局 3 胜
- 开始时一方先发球，直至判分，接下来胜者发球
- 球员只能在发球局得分，15 分胜一局
"""
import random


def print_info():
    """
    打印程序的介绍性信息
    :return:
    """
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值(以0到1之间的小数表示)")
    return


def input_params():
    """
    获得程序运行参数
    :return: 选手 A / B 的能力值，以及比赛局数
    """
    pro_a = eval(input("请输入选手 A 的能力值(0-1)："))
    pro_b = eval(input("请输入选手 B 的能力值(0-1)："))
    n = eval(input("模拟比赛的场次："))
    return pro_a, pro_b, n


def sim_games(pro_a, pro_b, n):
    """
    利用球员A和B的能力值，模拟n局比赛
    :param pro_a: 选手 A 的能力值
    :param pro_b: 选手 B 的能力值
    :param n: 比赛局数
    :return: 选手 A / B 的获胜局数
    """
    wins_a, wins_b = 0, 0
    for i in range(n):
        score_a, score_b = sim_game(pro_a, pro_b)
        print("模拟第 {} 局比赛：A {} 分 <---> B {} 分".format(i+1, score_a, score_b), end="")
        if score_a > score_b:
            wins_a += 1
            print(" ===> A 获胜！")
        else:
            wins_b += 1
            print(" ===> B 获胜！")
    return wins_a, wins_b


def sim_game(pro_a, pro_b):
    """
    利用球员A和B的能力值，模拟一局比赛
    :param pro_a: 选手 A 能力值
    :param pro_b: 选手 B 能力值
    :return: 选手 A / B 的得分
    """
    score_a, score_b = 0, 0
    serving = 'A'
    while score_a < 15 and score_b < 15:
        if serving == 'A':
            if random.random() < pro_a:
                score_a += 1
            else:
                serving = 'B'
        else:
            if random.random() < pro_b:
                score_b += 1
            else:
                serving = 'A'
    return score_a, score_b


def print_summary(wins_a, wins_b):
    """
    输出球员A和B获胜比赛的场次及概率
    :param wins_a: 选手 A 的得分
    :param wins_b: 选手 B 的得分
    :return:
    """
    n = wins_a + wins_b
    print("模拟比赛结束，共模拟 {} 局比赛".format(n))
    print("选手 A 获胜 {} 场比赛，占比 {:0.1%}".format(wins_a, wins_a/n))
    print("选手 B 获胜 {} 场比赛，占比 {:0.1%}".format(wins_b, wins_b/n))
    return


def main():
    """
    程序入口
    :return:
    """
    print_info()
    pro_a, pro_b, n = input_params()
    wins_a, wins_b = sim_games(pro_a, pro_b, n)
    print_summary(wins_a, wins_b)


main()
