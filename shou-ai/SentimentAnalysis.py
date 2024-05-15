#!/usr/bin/python3

"""
情感分析

基于情感分析库 SNOWNLP 分析客户评价文本的情感

第三方库：snownlp
"""

import snownlp


def analysis(file_path, print_analysis=False, print_result=False, print_final=True):
    """
    读取数据文件，使用 SNOWNLP 库进行分析，输出结果
    :param file_path: 数据文件路径
    :return:
    """
    f = open(file_path, "r", encoding="UTF-8")
    lines = f.readlines()
    f.close()
    result = []
    print("----开始分析----")
    for line in lines:
        line = line.strip()
        nlp = snownlp.SnowNLP(line)
        if print_analysis:
            print("[{}]: {}".format(nlp.sentiments, nlp.doc))
        result.append((nlp.sentiments, nlp.doc))
    print("----输出结果----")
    result.sort(key=lambda item: item[0])
    score = 0
    count = len(result)
    for i in range(count):
        if print_result:
            print("[{}]: {}".format(result[i][0], result[i][1]))
        if 0 < i < (count - 1):
            score += result[i][0]
    print("----最终结果----")
    if print_final:
        print("final score: {}".format(score / (count - 2)))


analysis("comment_good.txt", True, True, True)
analysis("comment_bad.txt", True, True, True)
