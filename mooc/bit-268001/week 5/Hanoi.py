#!/usr/bin/python3

"""
汉诺塔实践

汉诺塔问题大家都清楚，这里不再赘述。

完成如下功能：
有三个圆柱A、B、C，初始时A上有N个圆盘，N由用户输入给出，最终移动到圆柱C上。
每次移动步骤的表达方式示例如下：[STEP  10] A->C。其中，STEP是步骤序号，宽度为4个字符，右对齐。

请编写代码，获得输入N后，输出汉诺塔移动的步骤
"""

step = 0


def hanoi(src, des, mid, n):
    global step
    if n == 1:
        step += 1
        print("[STEP{:>4}] {}->{}".format(step, src, des))
    else:
        hanoi(src, mid, des, n - 1)
        step += 1
        print("[STEP{:>4}] {}->{}".format(step, src, des))
        hanoi(mid, des, src, n - 1)


hanoi("A", "C", "B", eval(input()))
