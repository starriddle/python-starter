#!/usr/bin/python3

"""
实例10：文本词频统计 -- 人物出场统计

参考附件：中文文本 三国演义.txt
请统计 三国演义.txt 文件中出现的人物，统计并输出出现最多的15个人物，注意：
(1) 使用 jieba 库进行中文文本分词
(2) 多个人物词语可能指向同一个人物
(3) 只需要人物词语，因此需要去除非人物词语
(4) 输出15个人物词语，每个单词一行
"""

import jieba

f = open("三国演义.txt", "r", encoding="utf-8")
text = f.read()
f.close()
words = jieba.lcut(text)
counts = {}
# 根据词频统计，不停排除非人物词语，直至统计出词频前15的人物词语
excludes = {"将军", "却说", "丞相", "二人", "不可", "荆州", "不能", "如此",
            "商议", "如何", "主公", "军士", "左右", "军马", "引兵", "次日",
            "大喜", "天下", "东吴", "于是", "今日", "不敢", "魏兵", "陛下",
            "一人", "都督", "人马", "不知", "汉中", "只见", '众将', '后主',
            '蜀兵', '上马', '大叫', '太守', '此人', '夫人', '先主', '后人',
            '背后', '城中', '天子', '一面', '何不', '大军', '忽报', '先生',
            '百姓', '何故', '然后', '先锋', '不如', '赶来'}
for word in words:
    if len(word) == 1:
        continue
    if word in excludes:
        continue
    if word == "诸葛亮" or word == "孔明曰":
        word = "孔明"
    elif word == "关公" or word == "云长":
        word = "关羽"
    elif word == "玄德" or word == "玄德曰":
        word = "刘备"
    elif word == "孟德":
        word = "曹操"
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(15):
    # name, count = items[i]
    # print("{:<10}{:>5}".format(name, count))
    print(items[i][0])
