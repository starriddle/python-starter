#!/usr/bin/python3

"""
《沉默的羔羊》之最多单词

附件是《沉默的羔羊》中文版内容，请读入内容，分词后输出长度大于等于2且出现频率最多的单词。
如果存在多个单词出现频率一致，请输出按照Unicode排序后最大的单词。

"""

import jieba

f = open("沉默的羔羊.txt", "r", encoding="utf-8")
text = f.read()
f.close()
words = jieba.lcut(text)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
word, count = items[0]
for item in items:
    if item[1] < count:
        break
    if item[0] > word:
        word = item[0]
print(word)
